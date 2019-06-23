# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 12:08:43 2018

@author: ls
"""
import re

def mesh_sweep(get):
    x_start = re.findall(r'//#SetMesh X(.+?)--',get)
    x_end = re.findall(r'--(.+?)Y',get)
    y_start = re.findall(r'Y(.+?)--',get)
    y_end = re.findall(r'--(\d+?)Z',get)
    z_start = re.findall(r'Z(.+?)--',get)
    z_end = re.findall(r'--(\d+?)x',get)
    x_cell = re.findall(r'x(.+?)y',get)
    y_cell = re.findall(r'y(.+?)z',get)
    z_cell = re.findall(r'z(.+?)i',get)
    x_pbc = re.findall(r'i(.+?)j',get)
    y_pbc = re.findall(r'j(.+?)k',get)
    z_pbc = re.findall(r'k(.+?)#by',get)
    x_step = re.findall(r'#by(.+?)by',get)
    y_step = re.findall(r'[0-9]by(.+?)by',get)
    z_step = re.findall(r'by(\d+?)#//',get)
    return x_start[0],x_end[0],y_start[0],y_end[0], \
    z_start[0],z_end[0],x_cell[0],y_cell[0],z_cell[0], \
    x_pbc[0],y_pbc[0],z_pbc[0],x_step[0],y_step[0],z_step[0]

def exc_sweep(get,exc_type):
    if exc_type == 'B':
        amp_start = re.findall(r'#amp_B := #(.+?)--',get)
        amp_end = re.findall(r'--(.+?)by amp',get)
        amp_step = re.findall(r'by amp(.+?)#\n//#f_B',get)
        f_start = re.findall(r'\n//#f_B := #(.+?)--',get)
        f_end = re.findall(r'--(.+?)by f',get)
        f_step = re.findall(r'by f(.+?)#//',get)
    elif exc_type == 'J':
        amp_start = re.findall(r'#amp_J := #(.+?)--',get)
        amp_end = re.findall(r'--(.+?)by amp',get)
        amp_step = re.findall(r'by amp(.+?)#\n//#f_J',get)
        f_start = re.findall(r'\n//#f_J := #(.+?)--',get)
        f_end = re.findall(r'--(.+?)by f',get)
        f_step = re.findall(r'by f(.+?)#//',get)
    return amp_start[0],amp_end[0],amp_step[0], \
    f_start[0],f_end[0],f_step[0]


def main(name,Dir,monitor):
    name = name.get()
    Dir = Dir.get()
    s1 = monitor.get('1.0','end')
    get1 = monitor.get('1.0','6.0')
    get2 = monitor.get('6.0','end')
    if_mesh_sweep = re.findall('//#',get1)
    if_exc_sweep = re.findall('//#',get2)
    
    if len(if_mesh_sweep) != 0 and len(if_exc_sweep) != 0:
        x0,x1,y0,y1,z0,z1,x_c,y_c,z_c,x_p,y_p,z_p,x_s,y_s,z_s=mesh_sweep(get1)
        x0,x1,y0,y1,z0,z1,x_s,y_s,z_s = int(x0),int(x1),int(y0),int(y1), \
        int(z0),int(z1),int(x_s),int(y_s),int(z_s)
        if '//#amp_B' in s1:
            exc_type = 'B'
        else:
            exc_type = 'J'
        amp0,amp1,amp_s,f0,f1,f_s = exc_sweep(get2,exc_type)
        amp0,amp1,amp_s,f0,f1,f_s = float(amp0),float(amp1), \
        float(amp_s),float(f0),float(f1),float(f_s)
        amp0,amp1,f0,f1 = round(amp0/amp_s),round(amp1/amp_s), \
        round(f0/f_s),round(f1/f_s)
        for x in range(x0, x1 + x_s, x_s):
            for y in range(y0, y1 + y_s, y_s):
                for z in range(z0, z1 + z_s, z_s):
                    for amp in range(amp0, amp1+1):
                        for f in range(f0, f1+1):
                            amp = amp*amp_s
                            f = f*f_s
                            s = s1
                            A = '{:.1e}'.format(amp)
                            F = '{:.1e}'.format(f)
                            
                            file_name = name+'_'+str(x)+'_'+str(y)+ \
                            '_'+str(z)+'_'+A+'_'+F+'.txt'
                            
                            mesh = 'setmesh('+str(x)+','+str(y)+',' \
                            +str(z)+','+x_c+','+y_c+','+z_c+','+ \
                            x_p+','+y_p+','+z_p+')'
                            # test
                            x_rep = '('+str(x*float(x_c))
                            y_rep = ','+str(y*float(y_c))
                            z_rep = ','+str(z*float(z_c))
                            
                            if exc_type == 'B':
                                A = 'amp_B := ' + A
                                F = 'f_B := ' + '2*pi*'+ F
                                exc_rep = re.findall(r'//#amp_B := #(.+?)#//',
                                                     get2,re.S)
                                s = s.replace('//#amp_B := #','')
                            else:
                                A = 'amp_J := ' + A
                                F = 'f_J := ' + '2*pi*'+ F
                                exc_rep = re.findall(r'//#amp_J := #(.+?)#//',
                                                     get2,re.S)
                                s = s.replace('//#amp_J := #','')
                            exc = A+'\n'+ F
                            
                            mesh_rep = re.findall(r'//#SetMesh X(.+?)#//',
                                                  get1)
                            
                            s = s.replace(mesh_rep[0],mesh)
                            #test
                            s = s.replace('(x',x_rep)
                            s = s.replace(',y',y_rep)
                            s = s.replace(',z',z_rep)
                            
                            s = s.replace(exc_rep[0],exc)
                            s = s.replace('//#SetMesh X','')
                            s = s.replace('#//','')
                            
                            file_name = Dir + '\\' + file_name
                            file = open(file_name, 'w')
                            file.writelines(s)
                            file.close()
    
    elif len(if_mesh_sweep) != 0 and len(if_exc_sweep) == 0:
        x0,x1,y0,y1,z0,z1,x_c,y_c,z_c,x_p,y_p,z_p,x_s,y_s,z_s=mesh_sweep(get1)
        x0,x1,y0,y1,z0,z1,x_s,y_s,z_s = int(x0),int(x1),int(y0),int(y1), \
        int(z0),int(z1),int(x_s),int(y_s),int(z_s)
        for x in range(x0, x1 + x_s, x_s):
            for y in range(y0, y1 + y_s, y_s):
                for z in range(z0, z1 + z_s, z_s):
                    
                    s = s1
                    file_name = name+'_'+str(x)+'_'+str(y)+ \
                    '_'+str(z)+'.txt'
                            
                    mesh = 'setmesh('+str(x)+','+str(y)+',' \
                    +str(z)+','+x_c+','+y_c+','+z_c+','+ \
                    x_p+','+y_p+','+z_p+')'
                    # test
                    x_rep = '('+str(x*float(x_c))
                    y_rep = ','+str(y*float(y_c))
                    z_rep = ','+str(z*float(z_c))
                    
                    mesh_rep = re.findall(r'//#SetMesh X(.+?)#//',
                                          get1)
                    s = s.replace(mesh_rep[0],mesh)
                    #test
                    s = s.replace('(x',x_rep)
                    s = s.replace(',y',y_rep)
                    s = s.replace(',z',z_rep)
                    
                    s = s.replace('//#SetMesh X','')
                    s = s.replace('#//','')
                    
                    file_name = Dir + '\\' + file_name
                    file = open(file_name, 'w')
                    file.writelines(s)
                    file.close()
    
    elif len(if_mesh_sweep) == 0 and len(if_exc_sweep) != 0:
        if '//#amp_B' in s1:
            exc_type = 'B'
        else:
            exc_type = 'J'
        amp0,amp1,amp_s,f0,f1,f_s = exc_sweep(get2,exc_type)
        amp0,amp1,amp_s,f0,f1,f_s = float(amp0),float(amp1), \
        float(amp_s),float(f0),float(f1),float(f_s)
        amp0,amp1,f0,f1 = round(amp0/amp_s),round(amp1/amp_s), \
        round(f0/f_s),round(f1/f_s)
        for amp in range(amp0, amp1+1):
            for f in range(f0, f1+1):
                amp = amp*amp_s
                f = f*f_s
                s = s1
                A = '{:.1e}'.format(amp)
                F = '{:.1e}'.format(f)
                            
                file_name = name+A+'_'+F+'.txt'
                
                if exc_type == 'B':
                    A = 'amp_B := ' + A
                    F = 'f_B := ' + '2*pi*'+ F
                    exc_rep = re.findall(r'//#amp_B := #(.+?)#//',
                                         get2,re.S)
                    s = s.replace('//#amp_B := #','')
                else:
                    A = 'amp_J := ' + A
                    F = 'f_J := ' + '2*pi*'+ F
                    exc_rep = re.findall(r'//#amp_J := #(.+?)#//',
                                         get2,re.S)
                    s = s.replace('//#amp_J := #','')
                exc = A+'\n'+F
                s = s.replace(exc_rep[0],exc)
                s = s.replace('#//','')
                
                file_name = Dir + '\\' + file_name
                file = open(file_name, 'w')
                file.writelines(s)
                file.close()
    
    else:
        file_name = Dir + '\\' + name + '.txt'
        file = open(file_name, 'w')
        file.writelines(s1)
        file.close()

        