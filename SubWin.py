# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 15:52:44 2018

@author: zhiwei ren
"""

import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from functions import *

class SubWin(tk.Toplevel):
    def __init__(self,size='940x600'):
        # win parameters
        super().__init__()
        self.mesh_count = 0
        self.shape_count = 0
        self.region_count = 1
        self.last_para = ''
        self.reset = True
        self.geometry(size)
        self.resizable(False,False)
    
    def name(self,name='subwin'):
        self.title(name)
    
    def monitor(self,monitor_h=20,monitor_w=56,c=1,r=0,
                monitor_padx=0,monitor_pady=15):
        monitor = scrolledtext.ScrolledText(self,font=('Arial',11),
                                            height=monitor_h,width=monitor_w,
                                            undo=True,wrap=tk.WORD)
        monitor.grid(column=c,row=r,rowspan=5,columnspan=3,
                     padx=monitor_padx,pady=monitor_pady)
        return monitor
    
    def frame(self,name='frame',c=0,r=0,rspan=6,
              cspan=1,frame_padx=10,frame_pady=10):
        f = ttk.LabelFrame(self,text=name)
        f.grid(column=c,row=r,rowspan=rspan,columnspan=cspan,
               padx=frame_padx,pady=frame_pady)
        return f
    
    @staticmethod
    def sub_frame(frame,name='frame',c=0,r=0,rspan=1,cspan=1):
        f = ttk.LabelFrame(frame,text=name)
        f.grid(column=c,row=r,rowspan=rspan,columnspan=cspan)
        return f
    
    def button(self,name,func,c,r,button_padx,button_pady):
        b = tk.Button(self,text=name,command=func,
                      font=('Aria', 14),width=15,height=2)
        b.grid(column=c,row=r,padx=button_padx,pady=button_pady)
        return b
    
    @staticmethod
    def sub_button(frame,name,func,c,r,cspan=2,w=18):
        b = tk.Button(frame,text=name,command=func,
                      font=('Aria',12),width=w,height=1)
        b.grid(column=c,row=r,columnspan=cspan)
        return b
    
    @staticmethod
    def entry(frame,var,w,c,r):
        e = ttk.Entry(frame,textvariable=var,width=w)
        e.grid(column=c,row=r)
        return e
    
    @staticmethod
    def combobox(frame,var,combo_type,c,r,w=12):
        cb = ttk.Combobox(frame,textvariable=var,width=w)
        if combo_type == 'shape':
            cb['values'] = ('Cell','Circle','Cuboid','Cylinder',
            'Ellipse','Ellipsoid','GrainRoughness','ImageShape',
            'Layer','Layers','None','Rect','Square','Universe',
            'XRange','YRange','ZRange')
        elif combo_type == 'method':
            cb['values'] = ('Add','Intersect','Inverse','None',
              'Repeat','RotX','RotY','RotZ','Scale','Sub',
              'Transl','Xor')
        elif combo_type == 'parameter':
            cb['values'] = ('Aex','alpha','anisC1','anisC2',
              'anisU','Dbulk','Dind','EpsilonPrime','FixedLayer',
              'frozenspins','Kc1','Kc2','Kc3','Ku1','Ku2','Lambda',
              'Msat','NoDemagSpins','Pol','Temp','xi')
        elif combo_type == 'm':
            cb['values'] = ('Antivortex','BlochSkyrmion','LoadFile',
              'NeelSkyrmion','None','RandomMag','RandomMagSeed',
              'TwoDomain','Uniform','Vortex','VortexWall')
        elif combo_type == 'method_m':
            cb['values'] = ('Add','None','RotZ','Scale',
              'SetRegion','Transl')
        elif combo_type == 'method_para':
            cb['values'] = ('Average','GetRegion','IsUniform','None',
              'Region','Set','SetRegion','SetRegionFn',
              'SetRegionFuncGo','SetRegionValueGo')
        elif combo_type == 'ext':
            cb['values'] = ('Add','AddGo','AddTo','Average','Comp',
              'IsUniform','None','Region','RemoveExtraTerms','Set',
              'SetRegion')
        elif combo_type == 'ext_misc':
            cb['values'] = ('Index2Coord','LoadFile','NewSlice')
        elif combo_type == 'output':
            cb['values'] = ('AutoSave','AutoSnapshot','FilenameFormat',
              'Fprintln','Print','Save','SaveAs',
              'Snapshot','SnapshotFormat','sprint','sprintf',
              'TableAdd','TableAddVar','TableAutoSave','TablePrint',
              'TableSave')
        elif combo_type == 'format':
            cb['values'] = ('OVF1_BINARY','OVF1_TEXT',
              'OVF2_BINARY','OVF2_TEXT')
        elif combo_type == 'slice':
            cb['values'] = ('Crop','CropLayer','CropX','CropY',
              'CropZ','None')
        elif combo_type == 'quantity':
            cb['values'] = ('B_anis','B_demag','B_eff','B_exch','B_ext',
              'B_therm','dt','E_anis','E_demag','E_exch','E_therm',
              'E_total','E_Zeeman','Edens_anis','Edens_demag',
              'Edens_exch','Edens_therm','Edens_total','Edens_Zeeman',
              'ExchCoupling','geom','J','LastErr','LLtorque','m',
              'm_full','MFM','MaxAngle','maxTorque','NEval','None',
              'PeakErr','spinAngle','STtorque','torque','TotalShift')
        elif combo_type == 'quan_method':
            cb['values'] = ('Average','Comp','None','Region','Set')
        elif combo_type == 'run':
            cb['values'] = ('Minimize','Relax','Run','RunWhile',
              'Steps','FixDt','Headroom','MaxDt','MaxErr','MinDt',
              'MinimizerSamples','MinimizerStop','step','SetSolver')
        elif combo_type == 'mfm':
            cb['values'] = ('MFM','MFMDipole','MFMLift')
        elif combo_type == 'msw':
            cb['values'] = ('Shift','ShiftGeom','ShiftM','ShiftMagL',
              'ShiftMagR','ShiftRegions','TotalShift')
        elif combo_type == 'extension':
            cb['values'] = ('ext_bubbledist','ext_bubblepos',
              'ext_bubblespeed','ext_centerWall','ext_corepos',
              'ext_dwpos','ext_dwspeed','ext_dwtilt','ext_EnableUnsafe',
              'ext_makegrains','ext_rmSurfaceCharge',
              'ext_ScaleExchange','ext_topologicalcharge',
              'ext_topologicalchargedensity','EnableDemag',
              'Expect','ExpectV')
        elif combo_type == 'for':
            cb['values'] = ('one cycle','double cycle',
              'triple cycle')
        cb.grid(column=c,row=r)
        return cb
        
    @staticmethod
    def label(frame,name,c,r,cspan=1):
        l = ttk.Label(frame,text=name).grid(column=c,row=r,
                     columnspan=cspan)
        return l
    
    @staticmethod
    def tabcontrol(frame,name0='Fixed',name1='Sweep'):
        TabControl = ttk.Notebook(frame)
        tab0 = ttk.Frame(TabControl)
        TabControl.add(tab0,text=name0)
        tab1 = ttk.Frame(TabControl)
        TabControl.add(tab1,text=name1)
        TabControl.grid(column=0,row=0,padx=10,pady=10)
        return tab0,tab1
    
    @staticmethod
    def frame_child_pad(frame):
        for child in frame.winfo_children():
            child.grid_configure(padx=4,pady=4)
    
    def mesh_count_add(self):
        self.mesh_count += 1
        return self.mesh_count
    
    def mesh_count_reset(self):
        self.mesh_count = 0
        return self.mesh_count
    
    def region_count_add(self):
        self.region_count += 1
        return self.region_count
    
    def region_count_minus(self):
        self.region_count -= 1
        return self.region_count
    
    def region_count_reset(self):
        self.region_count = 1
        return self.region_count
    
    def set_last_para(self,para):
        self.last_para = para
        return self.last_para

# =============================================================================
#                          Mesh & Geometry
# =============================================================================
def mesh(text_monitor):
    mesh_win = SubWin()
    mesh_win.title('Mesh & Geometry')
    mesh_win.geometry('960x600')
    mesh_win.resizable(False,False)

    # monitor
    mesh_monitor = scrolledtext.ScrolledText(mesh_win,font=('Arial',11),
                                             height=20,width=56,
                                             wrap=tk.WORD,undo=True)
    mesh_monitor.grid(column=1,row=0,rowspan=5,
                      columnspan=3,padx=0,pady=15)
    
    # mesh frame
    mesh_f = ttk.LabelFrame(mesh_win,text=' Mesh')
    mesh_f.grid(column=0,row=0,rowspan=6,padx=10,pady=10)
    
    # tabcontrol
    TabControl = ttk.Notebook(mesh_f)
    fixed_tab = ttk.Frame(TabControl)
    TabControl.add(fixed_tab,text='Fixed')
    sweep_tab = ttk.Frame(TabControl)
    TabControl.add(sweep_tab,text='Sweep')
    TabControl.grid(column=0,row=0,padx=10,pady=10)

    # fixed size frame
    fixed_f = ttk.LabelFrame(fixed_tab,text='Fixed Size')
    fixed_f.grid(column=0,row=0,rowspan=3,padx=10,pady=10)
    
    ttk.Label(fixed_f,text='X (m):').grid(column=0,row=0)
    ttk.Label(fixed_f,text='Y (m):').grid(column=0,row=1)
    ttk.Label(fixed_f,text='Z (m):').grid(column=0,row=2)
    
    # mesh var
    mesh_e_width = 9
    x_e_var = tk.StringVar()
    y_e_var = tk.StringVar()
    z_e_var = tk.StringVar()
    x_start_e_var = tk.StringVar()
    y_start_e_var = tk.StringVar()
    z_start_e_var = tk.StringVar()
    x_end_e_var = tk.StringVar()
    y_end_e_var = tk.StringVar()
    z_end_e_var = tk.StringVar()
    x_step_e_var = tk.StringVar()
    y_step_e_var = tk.StringVar()
    z_step_e_var = tk.StringVar()
    x_cell_e_var = tk.StringVar()
    y_cell_e_var = tk.StringVar()
    z_cell_e_var = tk.StringVar()
    x_PBC_e_var = tk.StringVar()
    y_PBC_e_var = tk.StringVar()
    z_PBC_e_var = tk.StringVar()

    x_e = ttk.Entry(fixed_f,textvariable=x_e_var,width=mesh_e_width)
    x_e.grid(column=1,row=0)
    y_e = ttk.Entry(fixed_f,textvariable=y_e_var,width=mesh_e_width)
    y_e.grid(column=1,row=1)
    z_e = ttk.Entry(fixed_f,textvariable=z_e_var,width=mesh_e_width)
    z_e.grid(column=1,row=2)
    
    for child in fixed_f.winfo_children():
        child.grid_configure(padx=4,pady=4)

    # size sweep frame
    sweep_f = ttk.LabelFrame(sweep_tab,text='Size Sweep')
    sweep_f.grid(column=0,row=0,rowspan=3,padx=10,pady=10)
    
    ttk.Label(sweep_f,text='X (m):').grid(column=0,row=0)
    ttk.Label(sweep_f,text='Y (m):').grid(column=0,row=1)
    ttk.Label(sweep_f,text='Z (m):').grid(column=0,row=2)
    ttk.Label(sweep_f,text='to').grid(column=2,row=0)
    ttk.Label(sweep_f,text='to').grid(column=2,row=1)
    ttk.Label(sweep_f,text='to').grid(column=2,row=2)
    ttk.Label(sweep_f,text='by').grid(column=4,row=0)
    ttk.Label(sweep_f,text='by').grid(column=4,row=1)
    ttk.Label(sweep_f,text='by').grid(column=4,row=2)
        
    x_start_e = ttk.Entry(sweep_f,textvariable=x_start_e_var,
                          width=mesh_e_width)
    x_start_e.grid(column=1,row=0)
    y_start_e = ttk.Entry(sweep_f,textvariable=y_start_e_var,
                          width=mesh_e_width)
    y_start_e.grid(column=1,row=1)
    z_start_e = ttk.Entry(sweep_f,textvariable=z_start_e_var,
                          width=mesh_e_width)
    z_start_e.grid(column=1,row=2)
    x_end_e = ttk.Entry(sweep_f,textvariable=x_end_e_var,
                        width=mesh_e_width)
    x_end_e.grid(column=3,row=0)
    y_end_e = ttk.Entry(sweep_f,textvariable=y_end_e_var,
                        width=mesh_e_width)
    y_end_e.grid(column=3,row=1)
    z_end_e = ttk.Entry(sweep_f,textvariable=z_end_e_var,
                        width=mesh_e_width)
    z_end_e.grid(column=3,row=2)
    
    x_step_e = ttk.Entry(sweep_f,textvariable=x_step_e_var,
                        width=mesh_e_width)
    x_step_e.grid(column=5,row=0)
    y_step_e = ttk.Entry(sweep_f,textvariable=y_step_e_var,
                        width=mesh_e_width)
    y_step_e.grid(column=5,row=1)
    z_step_e = ttk.Entry(sweep_f,textvariable=z_step_e_var,
                        width=mesh_e_width)
    z_step_e.grid(column=5,row=2)
    
    for child in sweep_f.winfo_children():
        child.grid_configure(padx=4,pady=4)
    
    # cell frame
    cell_f = ttk.LabelFrame(mesh_f,text='Cell Size & PBC')
    cell_f.grid(column=0,row=3,rowspan=3,padx=10,pady=10)
    
    ttk.Label(cell_f,text='cell_x (m):').grid(column=0,row=0)
    ttk.Label(cell_f,text='cell_y (m):').grid(column=0,row=1)
    ttk.Label(cell_f,text='cell_z (m):').grid(column=0,row=2)
        
    x_cell_e = ttk.Entry(cell_f,textvariable=x_cell_e_var,
                         width=mesh_e_width)
    x_cell_e.grid(column=1,row=0)
    y_cell_e = ttk.Entry(cell_f,textvariable=y_cell_e_var,
                         width=mesh_e_width)
    y_cell_e.grid(column=1,row=1)
    z_cell_e = ttk.Entry(cell_f,textvariable=z_cell_e_var,
                         width=mesh_e_width)
    z_cell_e.grid(column=1,row=2)
    
    ttk.Label(cell_f,text='PBC_x:').grid(column=2,row=0)
    ttk.Label(cell_f,text='PBC_y:').grid(column=2,row=1)
    ttk.Label(cell_f,text='PBC_z:').grid(column=2,row=2)
    
    x_PBC_e = ttk.Entry(cell_f,textvariable=x_PBC_e_var,
                        width=mesh_e_width)
    x_PBC_e.grid(column=3,row=0)
    y_PBC_e = ttk.Entry(cell_f,textvariable=y_PBC_e_var,
                        width=mesh_e_width)
    y_PBC_e.grid(column=3,row=1)
    z_PBC_e = ttk.Entry(cell_f,textvariable=z_PBC_e_var,
                        width=mesh_e_width)
    z_PBC_e.grid(column=3,row=2)

    for child in cell_f.winfo_children():
        child.grid_configure(padx=4,pady=4)

    # geometry frame
    geom_f = ttk.LabelFrame(mesh_win,text=' Geometry')
    geom_f.grid(column=0,row=6,rowspan=2,padx=10,pady=10)
    
    # geom var
    combo_width = 12
    shape_cb_var = tk.StringVar()
    method_cb_var = tk.StringVar()
    name_e_var = tk.StringVar()
    smooth_cb_var = tk.StringVar()
    for_cb_var = tk.StringVar()
    
    # label
    ttk.Label(geom_f,text='Shape:').grid(column=0,row=0)
    ttk.Label(geom_f,text='Method:').grid(column=2,row=0)
    ttk.Label(geom_f,text='Image Name:').grid(column=0,row=2)
    ttk.Label(geom_f,text='Edge Smooth:').grid(column=0,row=1)
    ttk.Label(geom_f,text='Loop:').grid(column=0,row=3)
    
    # combo box and entry
    shape_cb = ttk.Combobox(geom_f,textvariable=shape_cb_var,
                            width=combo_width)
    shape_cb['values'] = ('Cell','Circle','Cuboid','Cylinder',
            'Ellipse','Ellipsoid','GrainRoughness','ImageShape',
            'Layer','Layers','None','Rect','Square','Universe',
            'XRange','YRange','ZRange')
    shape_cb.grid(column=1,row=0)
    
    method_cb = ttk.Combobox(geom_f,textvariable=method_cb_var,
                             width=combo_width)
    method_cb['values'] = ('Add','Intersect','Inverse','None',
             'Repeat','RotX','RotY','RotZ','Scale','Sub',
             'Transl','Xor')
    method_cb.grid(column=3,row=0)
    
    smooth_cb = ttk.Combobox(geom_f,textvariable=smooth_cb_var,
                             width=combo_width)
    smooth_cb['values'] = (0,1,2,3,4,5,6,7,8)
    smooth_cb.grid(column=1,row=1)
    
    for_cb = ttk.Combobox(geom_f,textvariable=for_cb_var,
                          width=combo_width)
    for_cb['values'] = ('None','one cycle','double cycle',
          'triple cycle')
    for_cb.grid(column=1,row=3,columnspan=1)
    add_shape_b = tk.Button(geom_f,text='Add shape',
                            command=lambda:add_shape_loop(mesh_win,shape_cb_var,
                                                     method_cb_var,
                                                     mesh_monitor,for_cb_var),
                            font=('Aria',12),width=15)
    add_shape_b.grid(column=2,row=3,columnspan=1)
    
    undo_b = tk.Button(geom_f,text='Undo',
                            command=lambda:undo(mesh_monitor,mesh_win),
                            font=('Aria',12),width=15)
    undo_b.grid(column=3,row=3,columnspan=1)
    
    image_name_e = ttk.Entry(geom_f,textvariable=name_e_var,
                             width=26)
    image_name_e.grid(column=1,row=2,columnspan=2)
    
    for child in geom_f.winfo_children():
        child.grid_configure(padx=4,pady=4)

    # total control button
    '''func'''
    add_mesh_b = tk.Button(mesh_win,text='Add This Mesh',
                           command=lambda:add_mesh(mesh_win,mesh_monitor,x_e_var,
                                                   y_e_var,z_e_var,x_start_e_var,
                                                   y_start_e_var,z_start_e_var,
                                                   x_end_e_var,y_end_e_var,
                                                   z_end_e_var,x_step_e_var,
                                                   y_step_e_var,z_step_e_var,
                                                   x_cell_e_var,y_cell_e_var,
                                                   z_cell_e_var,x_PBC_e_var,
                                                   y_PBC_e_var,z_PBC_e_var),
                           font=('Aria', 14),width=14,height=2)
    add_mesh_b.grid(column=1,row=6,padx=5,pady=5)
    
    '''func'''
    add_geom_b = tk.Button(mesh_win,text='Add This Geom',
                           command=lambda:add_geom(mesh_monitor,
                                                   smooth_cb_var,
                                                   name_e_var),
                           font=('Aria', 14),width=14,height=2)
    add_geom_b.grid(column=2,row=6,padx=5,pady=5)
    
    '''func'''
    cancel_b = tk.Button(mesh_win,text='Cancel & Quit',
                         command=lambda:cancel(mesh_win),
                         font=('Aria', 14),width=14,height=2)
    cancel_b.grid(column=1,row=7,padx=5,pady=5)
    
    '''func'''
    confirm_b = tk.Button(mesh_win,text='Confirm & Quit',
                         command=lambda:confirm(mesh_monitor,
                                                text_monitor,mesh_win),
                         font=('Aria', 14),width=14,height=2)
    confirm_b.grid(column=2,row=7,padx=5,pady=5)


# =============================================================================
#                          Define Regions
# =============================================================================
def region(text_monitor):
    region_win = SubWin('800x600')
    region_win.name('Regions')
    region_monitor = region_win.monitor(monitor_h=25,c=5)
    region_f = region_win.frame(name='Regions',c=2,cspan=3)
    
    region_win.label(region_f,'',0,0)
    region_win.label(region_f,'',0,1)
    
    region_win.label(region_f,'Shape:',1,0)
    region_win.label(region_f,'Method:',1,1)
    
    shape_cb_var = tk.StringVar()
    method_cb_var = tk.StringVar()
    
    shape_cb = region_win.combobox(region_f,shape_cb_var,
                                   'shape',2,0,17)
    method_cb = region_win.combobox(region_f,method_cb_var,
                                    'method',2,1,17)
    region_win.sub_button(frame=region_f,name='Add Shape',
                          func=lambda:add_shape(region_win,shape_cb_var,
                                                method_cb_var,
                                                region_monitor),
                          c=1,r=2)
    
    '''func'''
    region_win.button('Add This Region',
                      func=lambda:add_region(region_win,
                                             region_monitor),
                      c=5,r=8,button_padx=5,button_pady=5)
    region_win.button('Delete Region',
                      func=lambda:region_undo(region_win,region_monitor),
                      c=6,r=8,button_padx=5,button_pady=5)
    region_win.button('Cancel & Quit',func=lambda:cancel(region_win),
                      c=5,r=9,button_padx=5,button_pady=5)
    region_win.button('Confirm & Quit',
                      func=lambda:confirm(region_monitor,
                                          text_monitor,region_win),
                      c=6,r=9,button_padx=5,button_pady=5)
    
    region_win.frame_child_pad(region_f)
    

# =============================================================================
#                       Parameters & Initial m
# =============================================================================
def para(text_monitor):
    para_win = SubWin('800x600')
    para_win.name('Parameters & Initial m')
    para_monitor = para_win.monitor(monitor_h=25)
    
    para_f = para_win.frame(name='Parameters',c=0,r=2)
    initial_m_f = para_win.frame(name='Initial m',rspan=3)
    
    para_win.label(initial_m_f,'Initial m:',0,0)
    para_win.label(initial_m_f,'Method:',0,1)
    para_win.label(para_f,'Parameters:',0,0)
    para_win.label(para_f,'Function:',0,1)
    para_win.label(para_f,'Method:',0,2)
    
    
    initial_m_cb_var = tk.StringVar()
    method_m_cb_var = tk.StringVar()
    para_cb_var = tk.StringVar()
    method_para_cb_var = tk.StringVar()
    para_e_var = tk.StringVar()
    
    initial_m_cb = para_win.combobox(initial_m_f,initial_m_cb_var,
                                     'm',1,0,w=16)
    method_m_cb = para_win.combobox(initial_m_f,method_m_cb_var,
                                     'method_m',1,1,w=16)
    para_win.sub_button(frame=initial_m_f,name='Undo',
                        func=lambda:region_undo(para_win,para_monitor),
                        c=0,r=3)
    
    para_cb = para_win.combobox(para_f,para_cb_var,
                                'parameter',1,0,w=16)
    para_e = para_win.entry(para_f,var=para_e_var,w=18,c=1,r=1)
    method_para_cb = para_win.combobox(para_f,method_para_cb_var,
                                       'method_para',1,2,w=16)
    para_win.sub_button(frame=para_f,name='Undo',
                        func=lambda:region_undo(para_win,para_monitor),
                        c=0,r=3)
    '''func'''
    para_win.button('Add Initial m',
                    func=lambda:add_m(initial_m_cb_var,
                                      method_m_cb_var,
                                      para_monitor,para_win),
                    c=1,r=8,button_padx=5,button_pady=5)
    para_win.button('Add This Para',
                    func=lambda:add_para(para_win,para_monitor,
                                         para_cb_var,para_e_var,
                                         method_para_cb_var),
                    c=2,r=8,button_padx=5,button_pady=5)
    para_win.button('Cancel & Quit',func=lambda:cancel(para_win),
                    c=1,r=9,button_padx=5,button_pady=5)
    para_win.button('Confirm & Quit',
                    func=lambda:confirm(para_monitor,
                                        text_monitor,para_win),
                    c=2,r=9,button_padx=5,button_pady=5)
    
    para_win.frame_child_pad(para_f)
    para_win.frame_child_pad(initial_m_f)
    

# =============================================================================
#                            Excitations
# =============================================================================
def excitation(text_monitor):
    ext_win = SubWin()
    ext_win.name('Excitations')
    ext_monitor = ext_win.monitor(c=5)
    
    ext_f = ext_win.frame(name='Excitations',cspan=4)
    B_f = ext_win.sub_frame(frame=ext_f,name='B_ext',c=0,r=0,rspan=3)
    J_f = ext_win.sub_frame(frame=ext_f,name='J_ext',c=0,r=3,rspan=3)
    misc_f = ext_win.sub_frame(frame=ext_f,name='Misc',c=0,r=6)
    sweep_f = ext_win.frame(name='Parameters',r=6,cspan=4)
    
    Bext_func_e_var = tk.StringVar()
    Bext_method_cb_var = tk.StringVar()
    
    ext_win.label(frame=B_f,name='Function:',r=0,c=0)
    ext_win.label(frame=B_f,name='Method:',r=1,c=0)
    
    Bext_func_e = ext_win.entry(frame=B_f,var=Bext_func_e_var,
                                w=25,r=0,c=1)
    Bext_method_cb = ext_win.combobox(frame=B_f,var=Bext_method_cb_var,
                                      combo_type='ext',c=1,r=1,w=22)
    
    J_func_e_var = tk.StringVar()
    J_method_cb_var = tk.StringVar()
    
    ext_win.label(frame=J_f,name='Function:',r=0,c=0)
    ext_win.label(frame=J_f,name='Method:',r=1,c=0)
    
    J_func_e = ext_win.entry(frame=J_f,var=J_func_e_var,w=25,r=0,c=1)
    J_method_cb = ext_win.combobox(frame=J_f,var=J_method_cb_var,
                                   combo_type='ext',c=1,r=1,w=22)
    
    J_misc_cb_var = tk.StringVar()
    ext_win.label(frame=misc_f,name='Misc:',r=0,c=0)
    J_misc_cb = ext_win.combobox(frame=misc_f,var=J_misc_cb_var,
                                 combo_type='ext_misc',c=1,r=0,w=22)
    add_misc_b = tk.Button(misc_f,text='Add This Misc',
                           command=lambda:add_misc(J_misc_cb_var,
                                                   ext_monitor),
                           font=('Aria', 12),width=16,height=1)
    add_misc_b.grid(column=0,row=2,columnspan=2)
    
    
    fixed_tab,sweep_tab = ext_win.tabcontrol(sweep_f)
    fixed_f = ttk.LabelFrame(fixed_tab,text='Fixed Parameters')
    fixed_f.grid(column=0,row=0,rowspan=3,padx=10,pady=10)
    sweep_f = ttk.LabelFrame(sweep_tab,text='Sweep Parameters')
    sweep_f.grid(column=0,row=0,rowspan=3,padx=10,pady=10)
    
    ext_win.label(fixed_f,'amp:',c=0,r=0)
    ext_win.label(fixed_f,'f:',c=0,r=1)
    ext_win.label(sweep_f,'amp:',c=0,r=0)
    ext_win.label(sweep_f,'f:',c=0,r=1)
    ext_win.label(sweep_f,'to',c=2,r=0)
    ext_win.label(sweep_f,'to',c=2,r=1)
    ext_win.label(sweep_f,'by',c=4,r=1)
    ext_win.label(sweep_f,'by',c=4,r=0)
    
    entry_w = 9
    amp_var = tk.StringVar()
    f_var = tk.StringVar()
    amp_start_var = tk.StringVar()
    amp_end_var = tk.StringVar()
    amp_step_var = tk.StringVar()
    f_start_var = tk.StringVar()
    f_end_var = tk.StringVar()
    f_step_var = tk.StringVar()
    
    amp_e = ext_win.entry(fixed_f,amp_var,c=1,r=0,w=entry_w)
    f_e = ext_win.entry(fixed_f,f_var,c=1,r=1,w=entry_w)
    amp_start_e = ext_win.entry(sweep_f,amp_start_var,c=1,r=0,w=entry_w)
    amp_end_e = ext_win.entry(sweep_f,amp_end_var,c=3,r=0,w=entry_w)
    amp_step_e = ext_win.entry(sweep_f,amp_step_var,c=5,r=0,w=entry_w)
    f_start_e = ext_win.entry(sweep_f,f_start_var,c=1,r=1,w=entry_w)
    f_end_e = ext_win.entry(sweep_f,f_end_var,c=3,r=1,w=entry_w)
    f_step_e = ext_win.entry(sweep_f,f_step_var,c=5,r=1,w=entry_w)
    
    ext_win.sub_button(frame=ext_f,name='Undo',
                       func=lambda:region_undo(ext_win,ext_monitor),
                       c=0,r=8)
    
    ext_win.button('Add This B_ext',
                   func=lambda:add_B(ext_win,ext_monitor,Bext_func_e_var,
                                     Bext_method_cb_var,amp_var,f_var,
                                     amp_start_var,f_start_var,
                                     amp_end_var,f_end_var,
                                     amp_step_var,f_step_var),
                   c=5,r=9,button_padx=5,button_pady=5)
    ext_win.button('Add This J_ext',
                   func=lambda:add_J(ext_win,ext_monitor,J_func_e_var,
                                     J_method_cb_var,amp_var,f_var,
                                     amp_start_var,f_start_var,
                                     amp_end_var,f_end_var,
                                     amp_step_var,f_step_var),
                   c=6,r=9,button_padx=5,button_pady=5)
    ext_win.button('Cancel & Quit',func=lambda:cancel(ext_win),
                   c=5,r=10,button_padx=5,button_pady=5)
    ext_win.button('Confirm & Quit',
                   func=lambda:confirm(ext_monitor,
                                       text_monitor,ext_win),
                   c=6,r=10,button_padx=5,button_pady=5)
    
    ext_win.frame_child_pad(ext_f)
    ext_win.frame_child_pad(B_f)
    ext_win.frame_child_pad(J_f)
    ext_win.frame_child_pad(misc_f)
    ext_win.frame_child_pad(fixed_f)
    ext_win.frame_child_pad(sweep_f)
    
# =============================================================================
#                           Miscellaneous
# =============================================================================
def misc(text_monitor):
    misc_win = SubWin('800x600')
    misc_win.name('Miscellaneous')
    misc_monitor = misc_win.monitor(monitor_h=25)
    
    mfm_f = misc_win.frame(name='Magnetic Force Microscopy',
                           r=1,rspan=2)
    msw_f = misc_win.frame(name='Moving Simulation Window',rspan=2)
    extension_f = misc_win.frame(name='Extensions',r=2,rspan=2)
    for_f = misc_win.frame(name='For Loops',r=3,rspan=2)
    
    misc_win.label(frame=mfm_f,name='    MFM:   ',c=0,r=0)
    misc_win.label(frame=msw_f,name='Window Move:',c=0,r=0)
    misc_win.label(frame=extension_f,name='Extensions:',c=0,r=0)
    misc_win.label(frame=for_f,name=' For Loops: ',c=0,r=0)
    
    mfm_cb_var = tk.StringVar()
    msw_cb_var = tk.StringVar()
    extension_cb_var = tk.StringVar()
    for_cb_var = tk.StringVar()
    
    mfm_cb = misc_win.combobox(frame=mfm_f,var=mfm_cb_var,
                               combo_type='mfm',c=1,r=0,w=17)
    msw_cb = misc_win.combobox(frame=msw_f,var=msw_cb_var,
                               combo_type='msw',c=1,r=0,w=17)
    extension_cb = misc_win.combobox(frame=extension_f,
                                     var=extension_cb_var,
                                     combo_type='extension',
                                     c=1,r=0,w=17)
    for_cb = misc_win.combobox(frame=for_f,var=for_cb_var,
                               combo_type='for',c=1,r=0,w=17)
    
    misc_win.sub_button(frame=mfm_f,name='Add This MFM',
                        func=lambda:add_misc(mfm_cb_var,misc_monitor),
                        c=0,r=1)
    misc_win.sub_button(frame=msw_f,name='Add This MSW',
                        func=lambda:add_misc(msw_cb_var,misc_monitor),
                        c=0,r=1)
    misc_win.sub_button(frame=extension_f,name='Add This extension',
                        func=lambda:add_misc(extension_cb_var,
                                             misc_monitor),
                        c=0,r=1)
    misc_win.sub_button(frame=for_f,name='Add This ForLoop',
                        func=lambda:add_for(for_cb_var,misc_monitor),
                        c=0,r=1)
    
    misc_win.button('Cancel & Quit',func=lambda:cancel(misc_win),
                    c=1,r=6,button_padx=5,button_pady=5)
    misc_win.button('Confirm & Quit',
                    func=lambda:confirm(misc_monitor,
                                        text_monitor,misc_win),
                    c=2,r=6,button_padx=5,button_pady=5)
    
    misc_win.frame_child_pad(mfm_f)
    misc_win.frame_child_pad(msw_f)
    misc_win.frame_child_pad(extension_f)
    misc_win.frame_child_pad(for_f)

# =============================================================================
#                          Running & Output
# =============================================================================
def output(text_monitor):
    output_win = SubWin('800x600')
    output_win.name('Running & Output')
    output_monitor = output_win.monitor(monitor_h=25)
    
    output_f = output_win.frame(name='Scheduling Output',rspan=4)
    run_f = output_win.frame(name='Running',c=0,r=2)
    
    format_cb_var = tk.StringVar()
    output_type_cb_var = tk.StringVar()
    slice_cb_var = tk.StringVar()
    quantity_cb_var = tk.StringVar()
    method_cb_var = tk.StringVar()
    
    output_win.label(frame=output_f,name='Export Format:',r=0,c=0)
    output_win.label(frame=output_f,name='Output Type:',r=1,c=0)
    output_win.label(frame=output_f,name='Slicing:',r=2,c=0)
    output_win.label(frame=output_f,name='Quantities:',r=3,c=0)
    output_win.label(frame=output_f,name='Method:',r=4,c=0)
    
    format_cb = output_win.combobox(frame=output_f,
                                    var=format_cb_var,
                                    combo_type='format',c=1,
                                    r=0,w=17)
    output_type_cb = output_win.combobox(frame=output_f,
                                         var=output_type_cb_var,
                                         combo_type='output',c=1,
                                         r=1,w=17)
    slice_cb = output_win.combobox(frame=output_f,
                                   var=slice_cb_var,
                                   combo_type='slice',c=1,
                                   r=2,w=17)
    quantity_cb = output_win.combobox(frame=output_f,
                                      var=quantity_cb_var,
                                      combo_type='quantity',c=1,
                                      r=3,w=17)
    
    quantity_method_cb = output_win.combobox(frame=output_f,
                                             var=method_cb_var,
                                             combo_type='quan_method',
                                             c=1,r=4,w=17)
    
    
    run_cb_var = tk.StringVar()
    
    output_win.label(frame=run_f,name='  Running:  ',r=0,c=0)
    
    run_cb = output_win.combobox(frame=run_f,var=run_cb_var,
                                 combo_type='run',c=1,r=0,w=17)
    '''func'''
    output_win.button('Add This Output',
                      func=lambda:add_output(output_monitor,
                                             format_cb_var,
                                             output_type_cb_var,
                                             slice_cb_var,
                                             quantity_cb_var,
                                             method_cb_var),
                      c=1,r=8,button_padx=5,button_pady=5)
    output_win.button('Add This Run',
                      func=lambda:add_run(run_cb_var,output_monitor),
                      c=2,r=8,button_padx=5,button_pady=5)
    output_win.button('Cancel & Quit',func=lambda:cancel(output_win),
                      c=1,r=9,button_padx=5,button_pady=5)
    output_win.button('Confirm & Quit',
                      func=lambda:confirm(output_monitor,
                                          text_monitor,output_win),
                      c=2,r=9,button_padx=5,button_pady=5)
    
    output_win.frame_child_pad(output_f)
    output_win.frame_child_pad(run_f)

