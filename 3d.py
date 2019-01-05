import vtk
from vtk.util.colors import tomato

poly = [[0, 0, 0], [0, 10, 0], [40, 10, 0], [40, 90, 0], [0, 90, 0], [0, 100, 0],
          [100,100,0], [100,90,0], [60,90,0], [60,10,0], [100,10,0], [100,0,0],
          [0,0,1], [0,10,1], [40,10,1], [40,90,1], [0,90,1], [0,100,1],
          [100,100,1], [100,90,1], [60,90,1], [60,10,1], [100,10,1], [100,0,1]]

poly_2 = [[0,0,0], [0,10,0], [10,10,0], [10,0,0]]

polyData = vtk.vtkPolyData()

hea = vtk.vtkPolyLineSource()

"""i = 0
for _ in poly:
    hea.SetPoints(hea.SetPoint(i, poly[i][0], poly[i][1], poly[i][2]))
    i += 1"""
#hea.SetNumberOfPoints()
hea.SetPoint(0, poly_2[0][0], poly_2[0][1], poly_2[0][2])
print(hea.GetNumberOfPoints())

heaMapper = vtk.vtkPolyDataMapper()
heaMapper.SetInputData(hea.GetPoints())

heaActor = vtk.vtkActor()
heaActor.SetMapper(heaMapper)

ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

ren.SetBackground(0.1, 0.2, 0.4)
renWin.SetSize(200, 200)

ren.AddActor(heaActor)

iren.Initialize()

ren.ResetCamera()
ren.GetActiveCamera().Zoom(1.5)
renWin.Render()

iren.Start()