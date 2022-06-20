from capture import df

from bokeh.plotting import figure, output_file, show

from bokeh.models import HoverTool, ColumnDataSource
df["start_string"]=df["start"].dt.strftime("%Y-%m-%d-%H:%M:%S")
df["end_string"]=df["end"].dt.strftime("%Y-%m-%d-%H:%M:%S")
cds=ColumnDataSource(df)

p=figure(x_axis_type='datetime',height=100,width=500,sizing_mode='scale_both',title="Motion Graph")
p.yaxis.ticker.desired_num_ticks = 1

hover=HoverTool(tooltips=[("start","@start_string"),("end","@end_string")])
p.add_tools(hover)

q=p.quad(left="start",right="end",bottom=0,top=1,color="blue", source=cds)

output_file('Graph.html')

show(p)
