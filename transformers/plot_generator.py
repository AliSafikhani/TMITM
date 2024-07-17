import matplotlib.pyplot as plt
from django.db import connection
from django.shortcuts import render
import io
import base64
import numpy as np
import math
import matplotlib.pyplot as plt
import io
import base64

class PlotGenerator: 
    def generate_plot(self,request):
        if request.method == 'POST':
            serial_number = request.POST['sn']
        sn= f'tfr{serial_number}'
        with connection.cursor() as cursor:
            cursor.execute (f'SELECT * FROM {sn}  ') 
            results = cursor.fetchall()
        print((results[0][0])*2)
        print(len(results))
        pointofdga=len(results)
        ddppii=200
        H2=[]
        O2=[]
        N2=[]
        CO=[]
        CO2=[]
        CH4=[]
        C2H4=[]
        C2H6=[]
        C2H2=[]
        C3H6=[]
        C3H8=[]
        
        CUM=np.zeros(pointofdga)
        XC2H2=np.zeros(pointofdga)
        XC2H4=np.zeros(pointofdga)
        XCH4=np.zeros(pointofdga)
        BETA=np.zeros(pointofdga)
        ALFA=np.zeros(pointofdga)
        X=np.zeros(pointofdga)
        Y=np.zeros(pointofdga)
        for i in range (pointofdga):
            H2.append(results[i][0])
            O2.append(results[i][1])
            N2.append(results[i][2])
            CO.append(results[i][3])
            CO2.append(results[i][4])
            CH4.append(results[i][5])
            C2H4.append(results[i][6])
            C2H6.append(results[i][7])
            C2H2.append(results[i][8])
            C3H6.append(results[i][9])
            C3H8.append(results[i][10])
            CUM[i]=C2H2[i]+C2H4[i]+CH4[i]
            XC2H2[i]=(100*C2H2[i])/CUM[i]
            XC2H4[i]=(100*C2H4[i])/CUM[i]
            XCH4[i]=(100*CH4[i])/CUM[i]
            BETA[i]=(0.1*XC2H2[i])
            ALFA[i]=(math.sqrt(75)*(0.1*XCH4[i]))/10
        
            X[i]=((-5/math.sqrt(75))*ALFA[i])+10-BETA[i]
            Y[i]=ALFA[i]

            SX1=[0 ,10]
            SX2=[-0.2, -0.2]
            SY1=[5.1, 10]
            SY2=[8.68, 0.2]
            SZ1=[0, 4.9]
            SZ2=[0.2, 8.68]


        ###########################################
        points = np.array([
            [0,  0],          #0-p1
            [10, 0],        #1-p2
            [5, 8.66],        #2-p3
            [2.3, 0],         #3-p4
            [7.1, 0],         #4-p5
            [8.5, 0],         #5-p6
            [6.74, 3],         #6-p7
            [5.54, 2.68],         #7-p8
            [5.5, 5.54],        #8-p9
            [6.34, 4.06],        #9-p10
            [7.3, 3.98],        #10-p11
            [7.5, 4.32],        #11-p12
            [5.8, 6.58],        #12-p13
            [6, 6.92],        #13-p14
            [4.9, 8.48],        #14-p15
            [5.1, 8.48],        #15-p16
            [4.34, 7.52],         #16-p17
            [4.8, 8.3]])        #17-p18
        ###########################################

        m1=(points[1,1]-points[0,1])/(points[1,0]-points[0,0])
        m2=(points[2,1]-points[0,1])/(points[2,0]-points[0,0])
        m3=(points[2,1]-points[1,1])/(points[2,0]-points[1,0])
        m4=(points[3,1]-points[8,1])/(points[3,0]-points[8,0])
        m5=(points[7,1]-points[4,1])/(points[7,0]-points[4,0])
        m6=(points[6,1]-points[5,1])/(points[6,0]-points[5,0])
        m7=(points[9,1]-points[7,1])/(points[9,0]-points[7,0])
        m8=(points[11,1]-points[6,1])/(points[11,0]-points[6,0])
        m9=(points[16,1]-points[9,1])/(points[16,0]-points[9,0])
        m10=(points[17,1]-points[10,1])/(points[17,0]-points[10,0])
        m11=(points[13,1]-points[12,1])/(points[13,0]-points[12,0])
        m12=(points[15,1]-points[14,1])/(points[15,0]-points[14,0])
        m131=(points[7,1]-points[3,1])/(points[7,0]-points[3,0])
        m141=(points[6,1]-points[7,1])/(points[6,0]-points[7,0])
        Y1=np.zeros(pointofdga)
        Y2=np.zeros(pointofdga)
        Y3=np.zeros(pointofdga)
        Y4=np.zeros(pointofdga)
        Y5=np.zeros(pointofdga)
        Y6=np.zeros(pointofdga)
        Y7=np.zeros(pointofdga)
        Y8=np.zeros(pointofdga)
        Y9=np.zeros(pointofdga)
        Y10=np.zeros(pointofdga)
        Y11=np.zeros(pointofdga)
        Y12=np.zeros(pointofdga)
        Y131=np.zeros(pointofdga)
        Y141=np.zeros(pointofdga)
        failure=np.zeros(pointofdga)
        d1=0
        d2=0
        dt=0
        t3=0
        t2=0
        t1=0
        pd=0
        for i in range (pointofdga):
            Y1[i]=(m1*X[i]-m1*points[0,0]+points[0,1])
            Y2[i]=(m2*X[i]-m2*points[2,0]+points[2,1])
            Y3[i]=(m3*X[i]-m3*points[2,0]+points[2,1])
            Y4[i]=(m4*X[i]-m4*points[8,0]+points[8,1])
            Y5[i]=(m5*X[i]-m5*points[7,0]+points[7,1])
            Y6[i]=(m6*X[i]-m6*points[6,0]+points[6,1])
            Y7[i]=(m7*X[i]-m7*points[9,0]+points[9,1])
            Y8[i]=(m8*X[i]-m8*points[11,0]+points[11,1])
            Y9[i]=(m9*X[i]-m9*points[16,0]+points[16,1])
            Y10[i]=(m10*X[i]-m10*points[17,0]+points[17,1])
            Y11[i]=(m11*X[i]-m11*points[13,0]+points[13,1])
            Y12[i]=(m12*X[i]-m12*points[14,0]+points[14,1])
            Y131[i]=(m131*X[i]-m131*points[7,0]+points[7,1])
            Y141[i]=(m141*X[i]-m141*points[6,0]+points[6,1])
            if Y[i] <= Y2[i] and Y[i]<=Y9[i] and Y[i]>=Y1[i] and Y[i]>=Y4[i] :
                print('D1')
                d1=d1+1  
            elif Y[i] <= Y4[i] and Y[i]<=Y9[i] and  Y[i]>=Y7[i]  and Y[i]>=Y131[i] :
                print ('D2')
                d2=d2+1
            elif Y[i] <= Y5[i] and Y[i]<=Y131[i] and Y[i]>=Y1[i]:
                print ('D2')
                d2=d2+1
            elif Y[i] <= Y2[i] and Y[i]<=Y10[i] and Y[i]>=Y9[i] and Y[i]>=Y7[i]:
                print ('DT')
                dt=dt+1    
            elif Y[i]<= Y7[i] and Y[i]<=Y10[i] and Y[i]>=Y8[i] and Y[i]>=Y141[i]:
                print ('DT') 
                dt=dt+1
            elif Y[i] <= Y141[i] and Y[i]<=Y6[i] and Y[i]>=Y5[i] and Y[i]>=Y1[i]:
                print ('DT') 
                dt=dt+1
            elif Y[i] <= Y3[i] and Y[i]<=Y8[i] and Y[i]>=Y6[i] and Y[i]>=Y1[i]:
                print ('T3')
                t3=t3+1
            elif Y[i] <= Y3[i] and Y[i]<=Y11[i] and Y[i]>=Y10[i] and Y[i]>=Y8[i]:
                print ('T2')
                t2=t2+1
            elif Y[i] <= Y3[i] and Y[i]<=Y2[i] and Y[i]<=Y12[i] and Y[i]>=Y11[i] and Y[i]>=Y10[i]:
                print ('T1') 
                t1=t1+1
            elif Y[i] <= Y3[i] and Y[i]<=Y2[i] and Y[i]>=Y12[i] :
                print ('PD')
                pd=pd+1

        print('failure' , failure)
        ###########################################
        region_PD = points[[2,14,15],:]
        region_T1 = points[[12,13,15,14,17],:]
        region_T2 = points[[10,11,13,12],:]
        region_T3 = points[[1,5,6,11],:]
        region_D1 = points[[0,3,8,16],:]
        region_D2 = points[[3,4,7,9,8],:]
        region_DT = points[[4,5,6,10,17,16,9,7],:]
        ###########################################
        plt.style.use('ggplot')
        fig1, ax1 = plt.subplots()
        plt.plot(SX1,SX2,'b-', label='line 1', linewidth=1)
        plt.plot(SY1,SY2,'b-', label='line 1', linewidth=1)
        plt.plot(SZ1,SZ2,'b-', label='line 1', linewidth=1)
        ax1.fill(region_PD[:, 0], region_PD[:, 1], '#2e962d')
        ax1.fill(region_T1[:, 0], region_T1[:, 1], '#bebe12')
        ax1.fill(region_T2[:, 0], region_T2[:, 1], '#ff642b')
        ax1.fill(region_T3[:, 0], region_T3[:, 1], '#b46414')
        ax1.fill(region_D1[:, 0], region_D1[:, 1], '#10b4a7')
        ax1.fill(region_D2[:, 0], region_D2[:, 1], '#121eb4')
        ax1.fill(region_DT[:, 0], region_DT[:, 1], '#f217d0')
        plt.scatter(X,Y,s=100, c ="blue")



        label1 = np.array([5, -0.5])
        ax1.text(label1[0], label1[1], '%C2H2')
        label11 = np.array([10, -0.5])
        ax1.text(label11[0], label11[1], '0')
        label12 = np.array([-0.3, -0.5])
        ax1.text(label12[0], label12[1], '100')
        label2 = np.array([2,4.5]) 
        ax1.text(label2[0], label2[1], '%CH4')
        label21 = np.array([0,0.4]) 
        ax1.text(label21[0], label21[1], '0')
        label22 = np.array([4.5,8.4]) 
        ax1.text(label22[0], label22[1], '100')
        label3 = np.array([7.5,4.5])
        ax1.text(label3[0], label3[1], '%C2H4')
        label31 = np.array([5.3,8.4]) 
        ax1.text(label31[0], label31[1], '0')
        label22 = np.array([10,0.3]) 
        ax1.text(label22[0], label22[1], '100')
        ####################

        ax1.text(5, 8.5, 'PD',fontsize=12,color='BLACK')
        ax1.text(5.5,7.2, 'T1',fontsize=12,color='BLACK')
        ax1.text(6.7, 5, 'T2',fontsize=12,color='BLACK')
        ax1.text(8, 2, 'T3',fontsize=12,color='BLACK')
        ax1.text(3, 4, 'D1',fontsize=12,color='BLACK')
        ax1.text(4.5,2, 'D2',fontsize=12,color='BLACK')
        ax1.text(6.5, 2, 'DT',fontsize=12,color='BLACK')
        ################################################
        ax1.set_xlim(-1, 12)
        ax1.set_ylim(-1, 12)
        ax1.set_title("'dark_background' style sheet")
        test1= self._convert_plot_to_base64(fig1)
        #################################################
        # creating the dataset
        data = {'D1':d1, 'D2':d2, 'DT':dt, 'T3':t3, 'T2':t2,'T1':t1, 'PD':pd}
            
        courses = list(data.keys())
        values = list(data.values())
        fig2=plt.figure()
        plt.bar(courses, values, color ='red', 
            width = 0.4)
        plt.xlabel("failure")
        plt.ylabel("No. of failure")
        plt.title("failure detected by doau method")
        test2= self._convert_plot_to_base64(fig2)
        #################################################
        fig3=plt.figure()
        # plt.rcParams['figure.dpi']=100
        plt.plot(H2,'#1f77b4', label='H2', linewidth=1 )
        plt.plot(O2,'#ff7f0e', label='O2', linewidth=1)
        plt.plot(N2,'#2ca02c', label='N2', linewidth=1)
        plt.plot(CO,'#d62728', label='CO', linewidth=1)
        plt.plot(CO2,'#9467bd', label='CO2', linewidth=1)
        plt.plot(CH4,'#8c564b', label='CH4', linewidth=1)
        plt.plot(C2H4,'#e377c2', label='C2H4', linewidth=1)
        plt.plot(C2H6,'#7f7f7f', label='C2H6', linewidth=1)
        plt.plot(C2H2,'#bcbd22', label='C2H2', linewidth=1)
        plt.plot(C3H6,'#17becf', label='C3H6', linewidth=1)
        plt.plot(C3H8,'#b2996e', label='C3H8', linewidth=1)
        plt.legend()
        test3= self._convert_plot_to_base64(fig3)
        return(serial_number,test1,test2,test3)


        #################################################
    def _convert_plot_to_base64(self, fig):
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        image_png = buf.getvalue()
        buf.close()
        plt.close(fig)
        return base64.b64encode(image_png).decode('utf-8')
        


