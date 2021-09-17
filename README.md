# Auto_download_PTB
Automated download ECG .mat files and .info files from PTB database.  
:point_right:	 https://archive.physionet.org/cgi-bin/atm/ATM?fbclid=IwAR37FA2zF1cYzSy7i9xUYa2nXjG9wjTWept_T3kDmY62wXDepdPMD32MzOU

Store recordings by patient partition.

## Execution
 - Please redefine the save_direcotry in line 11 before running "Download_PTB.py".  
   ![image](https://user-images.githubusercontent.com/78803926/132704400-46508eb0-9d68-4008-8891-842a7a347510.png)
  
 - Run python file  
 
   ``` python3 Download_PTB.py```  
   
   

 - A function "plotATM.m" that reads .mat and .info files and plots the converted data was provided on physionet  
   :point_right:	 https://archive.physionet.org/physiotools/matlab/plotATM.m 
