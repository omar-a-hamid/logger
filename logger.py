import datetime


class logger: 

    def __init__(self, path):

        self.file = open(str(path),'r+')

        self.file_str = str(self.file.readlines())

        
        self.index_hash= self.file_str.rindex("#")
        self.index_eol = self.file_str.find('\\n',self.index_hash)
        
        #TODO: try except, or if index eol = -1 ---> self.index_hash+1 : self.index_eol

        self.log_number_str = self.file_str[self.index_hash+1 : self.index_eol]

        self.log_number = int(self.log_number_str)+1

        self.write()
        self.write("start of log #",0)
        
        self.write(str(self.log_number),2)



    def write(self,log_data="",eol_flag=1): # 0 doesnt terminate with \n 2 doesnt start with time stamp nor adds eol

        if log_data == "":

            self.file.write("\n")
            return
    
        if eol_flag==1 or eol_flag==0 :
            self.file.write("\n")
            self.file.write("[")
            self.file.write(str(datetime.datetime.now()))
            self.file.write("]   ")
        
        
        self.file.write(str(log_data))
        
        if eol_flag == 1:
            self.file.write("\n")

    def end_log(self):
         
        self.write()
        self.write("end of log #",0)
        self.write(str(self.log_number),2)
        self.write()
        self.file.close()

    def readlines(self): 

        return self.file.readlines()
