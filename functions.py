# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 15:38:45 2018

@author: ls
"""

import re

def confirm(monitor,main_monitor,window):
    get = '\n' + monitor.get('1.0','end')
    main_monitor.insert('insert',get)
    window.destroy()

def cancel(window):
    window.destroy()

def add_mesh(win,monitor,X,Y,Z,x_start,y_start,z_start,x_end,
             y_end,z_end,x_step,y_step,z_step,x_cell,
             y_cell,z_cell,x_pbc,y_pbc,z_pbc):
    
    x_backup,y_backup,z_backup = X,Y,Z
    x_step_backup,y_step_backup = x_step,y_step
    if x_step.get() == '' or y_step.get() == '':
        x_step.set('0')
        y_step.set('0')
        z_step.set('0')
        x_start.set('0')
        y_start.set('0')
        z_start.set('0')
        x_end.set('0')
        y_end.set('0')
        z_end.set('0')
    elif x_step.get() != '' and y_step.get() != '':
        X.set('0')
        Y.set('0')
        Z.set('0')
    x,y,z = float(X.get()),float(Y.get()),float(Z.get())
    x_start,y_start,z_start = float(x_start.get()), \
    float(y_start.get()),float(z_start.get())
    x_end,y_end,z_end = float(x_end.get()), \
    float(y_end.get()),float(z_end.get())
    x_step,y_step,z_step = float(x_step.get()), \
    float(y_step.get()),float(z_step.get())
    x_cell,y_cell,z_cell = float(x_cell.get()), \
    float(y_cell.get()),float(z_cell.get())
    x_pbc,y_pbc,z_pbc = x_pbc.get(),y_pbc.get(),z_pbc.get()
    
    x,y,z = str(round(x/x_cell)),str(round(y/y_cell)),str(round(z/z_cell))
    x_start,y_start,z_start = str(round(x_start/x_cell)), \
    str(round(y_start/y_cell)),str(round(z_start/z_cell))
    x_end,y_end,z_end = str(round(x_end/x_cell)),str(round(y_end/y_cell)), \
    str(round(z_end/z_cell))
    x_step,y_step,z_step = str(round(x_step/x_cell)),str(round(y_step/y_cell)), \
    str(round(z_step/z_cell))
    x_cell,y_cell,z_cell = str(x_cell),str(y_cell),str(z_cell)
    
    if x_step != '0' and y_step != '0':
        get = '//#SetMesh X'+x_start+'--'+x_end+'Y'+y_start+'--'+y_end+'Z'+ \
        z_start+'--'+z_end+'x'+x_cell+'y'+y_cell+'z'+z_cell+'i'+ \
        x_pbc+'j'+y_pbc+'k'+z_pbc+'#by'+x_step+'by'+y_step+'by'+z_step+'#//'
        
        monitor.insert('insert','\n'+get)
    else:
        get = 'SetMesh('+ x +','+ y +','+ z +','+x_cell+','+ \
        y_cell+','+z_cell+','+x_pbc+','+y_pbc+','+z_pbc+')'
        monitor.insert('insert','\n'+get)
    win.mesh_count = 0
    if x_step_backup.get() == '0' and y_step_backup.get() == '0':
        x_step_backup.set('')
        y_step_backup.set('')
    elif x_step_backup.get() != '0' and y_step_backup.get() != '0':
        x_backup.set('')
        y_backup.set('')
        z_backup.set('')
    
def add_for(item,monitor):
   if item.get() == 'one cycle':
       get = 'i_start1 := '+'\ni_limit1 := '+'\ni_step1 := '+ \
       '\nfor i:=i_start1; i<i_limit1; i+=i_step1{\n\n}'
   elif item.get() == 'double cycle':
       get = 'i_start2 := '+'\ni_limit2 := '+'\ni_step2 := '+ \
       '\nj_start2 := '+'\nj_limit2 := '+'\nj_step2 := '+ \
       '\nfor i:=i_start2; i<i_limit2; i+=i_step2{'+ \
       '\n\tfor j:=j_start2; j<j_limit2; j+=j_step2{\n\n\t}\n}'
   else:
       get = 'i_start3 := '+'\ni_limit3 := '+'\ni_step3 := '+ \
       '\nj_start3 := '+'\nj_limit3 := '+'\nj_step3 := '+ \
       '\nk_start3 := '+'\nk_limit3 := '+'\nk_step3 := '+ \
       '\nfor i:=i_start3; i<i_limit3; i+=i_step3{'+ \
       '\n\tfor j:=j_start3; j<j_limit3; j+=j_step3{'+\
       '\n\t\tfor k:=k_start3; k<k_limit3; k+=k_step3{\n\n\t\t}\n\t}\n}'
   monitor.insert('insert','\n'+'\n'+get)

def add_shape(win,shape,method,monitor):
    if shape.get() == 'None':
        get = '.' + method.get() + '()'
    elif method.get() == 'None' or method.get() == '':
        if win.mesh_count == 0:
            get = '\n' + shape.get() + '()'
            win.mesh_count_add()
        else:
            get = shape.get() + '()'
    else:
        if win.mesh_count == 0:
            get = '\n' + shape.get() + '().' + method.get() + '()'
            win.mesh_count_add()
        else:
            get = shape.get() + '().' + method.get() + '()'
    monitor.insert('insert',get)

def add_shape_loop(win,shape,method,monitor,loop):
    name_list = ['a:=','b:=','c:=','d:=','e:=','f:=','g:=',
                 'h:=','i:=','j:=','k:=','l:=','m:=','n:=',
                 'o:=','p:=','q:=','r:=','s:=','t:=','u:=',
                 'v:=','w:=','x:=','y:=','z:=']
    
    if shape.get() == 'None':
        get = '.' + method.get() + '()'
    elif method.get() == 'None' or method.get() == '':
        get = '\n' + name_list[win.mesh_count] + shape.get() + '()'
        win.mesh_count_add()
    else:
        get = '\n' + name_list[win.mesh_count] + shape.get() + '().' \
        + method.get() + '()'
        win.mesh_count_add()
    if loop.get() == 'None' or loop.get() == '':
        pass
    else:
        get = ''
        add_for(loop,monitor)
    monitor.insert('insert',get)

def undo(monitor,win):
    monitor.edit_undo()
    win.mesh_count_reset()

def add_geom(monitor,smooth,image_name):
    monitor_get = monitor.get('1.0','end')
    if_image = re.findall('ImageShape',monitor_get)
    if len(if_image) != 0:
        get = '\n'+'\nSetGeom(ImageShape("'+image_name.get()+'"))'
    else:
        get = '\n'+'\nSetGeom()'
    
    monitor.insert('insert',get)
    
    monitor.insert('insert','\nEdgeSmooth='+smooth.get())

def add_region(win,monitor):
    line_count = win.region_count + 1
    region_count = win.region_count
    monitor_get = monitor.get(str(line_count)+'.0','end-1c')
    get = '\nDefRegion('+str(region_count)+','+monitor_get+')'
    monitor.delete(str(line_count)+'.0','end')
    monitor.insert('insert',get)
    win.region_count_add()
    win.mesh_count = 0

def region_undo(win,monitor):
    monitor.edit_undo()
    if win.region_count == 1:
        pass
    else:
        win.region_count_minus()

def add_m(m,method,monitor,win):
    region_count = win.region_count
    m = m.get()
    method = method.get()
    monitor_get = monitor.get('1.0','end')
    if_region = re.findall('SetRegion',monitor_get)
    if len(if_region) != 0:
        if m == 'LoadFile':
            get = 'm.LoadFile("")'
        elif method == 'SetRegion':
            get = '\nm.'+method+'('+str(region_count)+','+m+'()'+')'
            win.region_count_add()
        elif m == 'None':
            get = '.'+method+'()'
        else:
            if method == '' or method == 'None':
                get = m+'()'
            else:
                get = m+'().'+method+'()'
    else:
        if method == 'SetRegion':
            get = '\nm.'+method+'('+str(region_count)+','+m+'()'+')'
            win.region_count_add()
        elif m == 'LoadFile':
            get = '\nm.LoadFile("")'
        elif m == 'None':
            get = '.'+method+'()'
        else:
            if method == '' or method == 'None':
                get = '\nm='+m+'()'
            else:
                get = '\nm='+m+'().'+method+'()'
    monitor.insert('insert',get)

def add_para(win,monitor,para,func,method):
    func = func.get()
    para = para.get()
    method = method.get()
    if win.reset == True:
        win.region_count_reset()
        win.reset = False
    else:
        pass

    if 'SetRegion' in method:
        if win.last_para == para or win.last_para =='':
            get = '\n'+para+'.'+method+'('+str(win.region_count)+',' \
            +func+')'
            win.region_count_add()
            win.set_last_para(para)
        else:
            win.region_count_reset()
            get = '\n'+para+'.'+method+'('+str(win.region_count)+',' \
            +func+')'
            win.set_last_para(para)
    elif method == '' or method == 'None':
        get = '\n'+para+'='+func
    else:
        get = '\n'+para+'.'+method+'()'
    monitor.insert('insert',get)

def alter_name(func,num,ext):
    b = 'amp'
    c = 'f'
    if num == -1:
        if ext == 'B':
            item = '_B'
        else:
            item = '_J'
    else:
        if ext == 'B':
            item = '_B'+str(num)
        else:
            item = '_J'+str(num)
    
    index1 = -3
    while index1 != -1:
        index1 = func.find(b,index1+3)
        func = list(func)
        if index1 != -1:
            func.insert(index1+3,item)
        else:
            pass
        func = ''.join(func)
    
    index2 = -2
    while index2 != -1:
        index2 = func.find(c,index2+2)
        func = list(func)
        if index2 != -1:
            func.insert(index2+1,item)
        else:
            pass
        func = ''.join(func)
    return func

def add_B(win,monitor,func,method,amp,f,amp_start,
          f_start,amp_end,f_end,amp_step,f_step):
    
    amp_step_backup,f_step_backup = amp_step,f_step
    amp_backup,f_backup = amp,f
    
    if amp_step.get() == '':
        amp_step.set('0')
        f_step.set('0')      
        amp_start.set('0')
        f_start.set('0') 
        amp_end.set('0')
        f_end.set('0')
    else:
        amp.set('0')
        f.set('0')
    
    func,method = func.get(),method.get()
    amp,f = amp.get(),f.get()
    amp_start,f_start = amp_start.get(),f_start.get()
    amp_end,f_end = amp_end.get(),f_end.get()
    amp_step,f_step = amp_step.get(),f_step.get()
    if win.reset == True:
        win.region_count_reset()
        win.reset = False
    else:
        pass
    
    if amp_step != '0' and f_step != '0':
        
        get = '//#amp_B := #'+amp_start+'--'+amp_end+' by amp'+ \
        amp_step+'#'+'\n//#f_B := #'+f_start+'--'+f_end+ \
        ' by f'+f_step+'#//'
        
        func = alter_name(func,-1,'B')
        if 'Add' in method:
            get = get + '\nB_ext.Add('+','+func+')'
        elif 'SetRegion' in method:
            get = get+'\nB_ext.'+method+'('+str(win.region_count)+',' \
            +func+')'
            win.region_count_add()
        elif method == '' or method == 'None':
            get = get+'\nB_ext='+func
        else:
            get = get+'\nB_ext.'+method+'()'
        
    else:
        if f == '':
            f = '0'
        else:
            pass
        get = 'amp_B := '+amp+'\nf_B := '+f
        
        if 'Add' in method:
            func = alter_name(func,-1,'B')
            get = get + '\nB_ext.Add('+','+func+')'
        elif 'SetRegion' in method:
            get = 'amp_B'+str(win.region_count)+' := '+amp+ \
            '\nf_B'+str(win.region_count)+' := '+f
            func = alter_name(func,win.region_count,'B')
            get = get+'\nB_ext.'+method+'('+str(win.region_count)+',' \
            +func+')'
            win.region_count_add()
        elif method == '' or method == 'None':
            func = alter_name(func,-1,'B')
            get = get+'\nB_ext='+func
        else:
            func = alter_name(func,-1,'B')
            get = get+'\nB_ext.'+method+'()'
    
    monitor.insert('insert','\n'+get)
    if amp_step_backup.get() == '0' and f_step_backup.get() == '0':
        amp_step_backup.set('')
        f_step_backup.set('')
    else:
        amp_backup.set('')
        f_backup.set('')

def add_J(win,monitor,func,method,amp,f,amp_start,
          f_start,amp_end,f_end,amp_step,f_step):
    
    amp_step_backup,f_step_backup = amp_step,f_step
    amp_backup,f_backup = amp,f
    
    if amp_step.get() == '' or f_step.get() == '':
        amp_step.set('0')
        f_step.set('0')      
        amp_start.set('0')
        f_start.set('0') 
        amp_end.set('0')
        f_end.set('0')
    else:
        amp.set('0')
        f.set('0')
    
    func,method = func.get(),method.get()
    amp,f = amp.get(),f.get()
    amp_start,f_start = amp_start.get(),f_start.get()
    amp_end,f_end = amp_end.get(),f_end.get()
    amp_step,f_step = amp_step.get(),f_step.get()
    if win.reset == True:
        win.region_count_reset()
        win.reset = False
    else:
        pass
    
    if amp_step != '0' and f_step != '0':
        
        get = '//#amp_J := #'+amp_start+'--'+amp_end+' by amp'+ \
        amp_step+'#'+'\n//#f_J := #'+f_start+'--'+f_end+ \
        ' by f'+f_step+'#//'
        func = alter_name(func,-1,'J')
        
        if 'Add' in method:
            get = get + '\nJ.Add('+','+func+')'
        elif 'SetRegion' in method:
            get = get+'\nJ.'+method+'('+str(win.region_count)+',' \
            +func+')'
            win.region_count_add()
        elif method == '' or method == 'None':
            get = get+'\nJ='+func
        else:
            get = get+'\nJ.'+method+'()'
        
    else:
        if f == '':
            f = '0'
        else:
            pass
        get = 'amp_J := '+amp+'\nf_J := '+f
        
        if 'Add' in method:
            func = alter_name(func,-1,'J')
            get = get + '\nJ.Add('+','+func+')'
        elif 'SetRegion' in method:
            get = 'amp_J'+str(win.region_count)+' := '+amp+ \
            '\nf_J'+str(win.region_count)+' := '+f
            func = alter_name(func,win.region_count,'J')
            get = get+'\nJ.'+method+'('+str(win.region_count)+',' \
            +func+')'
            win.region_count_add()
        elif method == '' or method == 'None':
            func = alter_name(func,-1,'J')
            get = get+'\nJ='+func
        else:
            func = alter_name(func,-1,'J')
            get = get+'\nJ.'+method+'()'
    
    monitor.insert('insert','\n'+get)
    if amp_step_backup.get() == '0' and f_step_backup.get() == '0':
        amp_step_backup.set('')
        f_step_backup.set('')
    else:
        amp_backup.set('')
        f_backup.set('')

def add_misc(misc,monitor):
    monitor.insert('insert','\n'+misc.get()+'()')

def add_output(monitor,form,out_type,slicing,quantity,method):
    get = ''
    if quantity.get() == 'None':
        quantity.set('')
    else:
        pass
    if form.get() == '':
        pass
    else:
        get = 'OutputFormat = '+form.get()
    
    out = out_type.get()
    if 'Save' in out or 'Snapshot' in out or out == 'TableAdd':
        if slicing.get() == '' or slicing.get() == 'None':
            if method.get() == '' or method.get() == 'None':
                get = get+'\n'+out+'('+quantity.get()+')'
            else:
                get = get+'\n'+out+'('+quantity.get()+ \
                '.'+method.get()+'())'
        else:
            if method.get() == '' or method.get() == 'None':
                get = get+'\n'+out+'('+slicing.get()+'('+ \
                quantity.get()+'))'
            else:
                get = get+'\n'+out+'('+slicing.get()+'('+ \
                quantity.get()+'.'+method.get()+'()))'
    else:
        get = get+'\n'+out+'()'
    monitor.insert('insert','\n'+get)
    
def add_run(run,monitor):
    run = run.get()
    if run == 'Minimize' or run == 'Relax' or run == 'Steps':
        get = run + '()'

    elif 'Run'in run or run == 'SetSolver':
        get = run + '()'
    else:
        get = run + ' ='
    monitor.insert('insert','\n'+get)

