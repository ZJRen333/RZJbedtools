'''
#coding:UTF-8
'''
import sys 
readfilename=sys.argv[1]
class Xtobedlist():
    def __init__(self,filename,indexlist):
        self.file=open(filename,'r')
        self.indexlist=indexlist
    def sublistabstract(self,listinput,indexlist):
        sublist=[]
        for i in indexlist:
            sublist.append(listinput[i])
        return sublist
    def fileread(self):
        listoutput=[]
        for str_x in self.file:
            list_x=str_x[:-1].split('\t')
            sublist=self.sublistabstract(list_x,self.indexlist)
            listoutput.append(sublist)
        return listoutput
    def filewrite(self,listinput,writefile):
        d=open(writefile,'a')
        for listx in listinput:
            str_write='\t'.join(listx)+'\n'
            d.writelines(str_write)
class XtoGTF(Xtobedlist):
    def __init__(self,filename,indexlist,insertindex):
        self.file=open(filename,'r')
        self.indexlist=indexlist
        self.insertindex=insertindex
    def listinsert(self,listinput,):
        listoutput=[]
        for listx in listinput:
            insertvalue=[listx[3],'exon','.','+','0','gene_id "'+listx[3]+'"']
            for i in len(self.insertindex):
                index_i=self.insertindex[i]
                value_i=self.insertvalue[i]
                listx.insert(index_i,value_i)
            listoutput.append(listx)
        return listoutput
def filenamesplit(filename):
    if filename.split('.')[1]=='broadPeak':
        indexlist=[0,1,2,3]
    if filename.split('.')[1]=='narrowPeak':
        indexlist=[0,1,2,3]
    return indexlist
def bedmain():
    dfile=readfilename.split('.')[0]+'.bed'
    indexlist=filenamesplit(readfilename)
    Instant=Xtobedlist(readfilename,indexlist)
    listwrite=Instant.fileread()
    Instant.filewrite(listwrite,dfile)
if __name__=='__main__':
    bedmain()
    
    
