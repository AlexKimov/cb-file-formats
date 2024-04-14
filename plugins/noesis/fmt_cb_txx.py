from inc_noesis import *

def registerNoesisTypes():
    handle = noesis.register("Captain Blood Textures", ".txx")

    noesis.addOption(handle, "-format", "image format", noesis.OPTFLAG_WANTARG)
    noesis.addOption(handle, "-version", "format version", noesis.OPTFLAG_WANTARG)
    noesis.addOption(handle, "-mipmapcount", "number of mipmaps", noesis.OPTFLAG_WANTARG)

    noesis.setHandlerTypeCheck(handle, cbCheckType)
    noesis.setHandlerLoadRGBA(handle, cbLoadRGBA)

    return 1
       
  
class CBImage:
    def __init__(self, reader):
        self.filereader = reader
        self.width = 0
        self.height = 0
        self.type = 0
 
    def parseHeader(self):
        self.filereader.seek(0, NOESEEK_ABS)
       
        self.magic = self.filereader.readUInt()    # TXX 
        self.version = self.filereader.readUInt()  # 1.0
        self.type = self.filereader.readUInt()  
        self.format = self.filereader.readUInt()  
        self.width = self.filereader.readUInt() 
        self.height = self.filereader.readUInt()  
        self.depth = self.filereader.readUInt()
        self.numMips = self.filereader.readUInt() 
        self.lineSize = self.filereader.readUInt() 
        self.bpp = self.filereader.readUInt() 
        self.fps = self.filereader.readUInt() 

        return 0            

    def getImageData(self):
        format = {1:"b8g8r8a8", 2:"b8g8r8a8", 3:"b5g6r5", 4:"b5g5r5a1", 5:"b4g4r4a4"}
            
        if self.format < 6: # RGB
            fmt = format[self.format]  
            if self.format < 3: 
                imageBuffer = self.filereader.readBytes(self.width * self.height * 4)
            else:                    
                imageBuffer = self.filereader.readBytes(self.width * self.height * 2)   
            self.data = rapi.imageDecodeRaw(imageBuffer, self.width, self.height, \
            fmt) 

        elif self.format > 8: # DXT
            if self.format == 9:
                self.data = self.filereader.readBytes(int(self.width * self.height / 2))
            else:       
                self.data = self.filereader.readBytes(self.width * self.height)               
 
    def read(self):
        self.parseHeader()
        if self.type == 1:    
            self.getImageData()
        
    
def cbCheckType(data):
    cbImage = CBImage(NoeBitStream(data))
    if cbImage.parseHeader() != 0:
        return 0
        
    return 1  


def cbLoadRGBA(data, texList):
    # noesis.logPopup() 
    cbImage = CBImage(NoeBitStream(data))       
    cbImage.read() 
    
    if cbImage.type == 1:
        if cbImage.format == 9:     
            texList.append(NoeTexture("cbtex", cbImage.width, cbImage.height, cbImage.data,
                                  noesis.NOESISTEX_DXT1))
        elif cbImage.format == 10:     
            texList.append(NoeTexture("cbtex", cbImage.width, cbImage.height, cbImage.data,
                                  noesis.NOESISTEX_DXT3))                                 
        elif cbImage.format == 11:     
            texList.append(NoeTexture("cbtex", cbImage.width, cbImage.height, cbImage.data,
                                  noesis.NOESISTEX_DXT5))
        else:     
            texList.append(NoeTexture("cbtex", cbImage.width, cbImage.height, cbImage.data,
                                  noesis.NOESISTEX_RGBA32))
            
    return 1
