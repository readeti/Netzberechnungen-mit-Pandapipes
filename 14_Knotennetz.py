import pandas as pd
import pandapipes as pp


# create an empty network
net = pp.create_empty_network(fluid ="lgas")



# fill it with elements
junction1 = pp.create_junction(net, pn_bar=1.013, tfluid_k=273.15, name="Junction 1", geodata=(0, 0))
junction2 = pp.create_junction(net, pn_bar=1.013, tfluid_k = 273.15, name="Junction 2", geodata=(2, 0))
junction3 = pp.create_junction(net, pn_bar=1.013, tfluid_k = 273.15, name="Junction 3", geodata=(4, 0))
junction4 = pp.create_junction(net, pn_bar=1.013, tfluid_k = 273.15, name="Junction 4", geodata=(6, 0))
junction5 = pp.create_junction(net, pn_bar=1.013, tfluid_k = 273.15, name="Junction 5", geodata=(8, 0))
junction6 = pp.create_junction(net, pn_bar=1.013, tfluid_k = 273.15, name="Junction 6", geodata=(10, 0))
junction7 = pp.create_junction(net, pn_bar=1.013, tfluid_k = 273.15, name="Junction 7", geodata=(8, 2))
junction8 = pp.create_junction(net, pn_bar=1.013, tfluid_k = 273.15, name="Junction 8", geodata=(6, 2))
junction9 = pp.create_junction(net, pn_bar=1.013, tfluid_k = 273.15, name="Junction 9", geodata=(4, 2))
junction10 = pp.create_junction(net, pn_bar=1.013, tfluid_k = 273.15, name="Junction 10", geodata=(2, 2))
junction11 = pp.create_junction(net, pn_bar=1.013, tfluid_k = 273.15, name="Junction 11", geodata=(2, 4))
junction12 = pp.create_junction(net, pn_bar=1.013, tfluid_k = 273.15, name="Junction 12", geodata=(4, 4))
junction13 = pp.create_junction(net, pn_bar=1.013, tfluid_k = 273.15, name="Junction 13", geodata=(8, 4))
junction14 = pp.create_junction(net, pn_bar=1.013, tfluid_k = 273.15, name="Junction 14", geodata=(4, 6))

ext_grid = pp.create_ext_grid(net, junction=junction1, p_bar=0.03, t_k=273.15, name="Grid Connection")

# create pipes
pipe1 = pp.create_pipe_from_parameters(net, from_junction=junction1, to_junction=junction2, length_km=0.026, diameter_m=0.30, k_mm=1, name="Pipe 1")
pipe2 = pp.create_pipe_from_parameters(net, from_junction=junction2, to_junction=junction3, length_km=0.080, diameter_m=0.25, k_mm=1, name="Pipe 2")
pipe3 = pp.create_pipe_from_parameters(net, from_junction=junction3, to_junction=junction4, length_km=0.144, diameter_m=0.25, k_mm=1, name="Pipe 3")
pipe4 = pp.create_pipe_from_parameters(net, from_junction=junction4, to_junction=junction5, length_km=0.192, diameter_m=0.25, k_mm=1, name="Pipe 4")
pipe5 = pp.create_pipe_from_parameters(net, from_junction=junction5, to_junction=junction6, length_km=0.106, diameter_m=0.15, k_mm=1, name="Pipe 5")
pipe6 = pp.create_pipe_from_parameters(net, from_junction=junction2, to_junction=junction10, length_km=0.096, diameter_m=0.30, k_mm=1, name="Pipe 6")
pipe7 = pp.create_pipe_from_parameters(net, from_junction=junction10, to_junction=junction9, length_km=0.148, diameter_m=0.25, k_mm=1, name="Pipe 7")
pipe8 = pp.create_pipe_from_parameters(net, from_junction=junction9, to_junction=junction8, length_km=0.080, diameter_m=0.20, k_mm=1, name="Pipe 8")
pipe9 = pp.create_pipe_from_parameters(net, from_junction=junction8, to_junction=junction7, length_km=0.076, diameter_m=0.15, k_mm=1, name="Pipe 9")
pipe10 = pp.create_pipe_from_parameters(net, from_junction=junction5, to_junction=junction7, length_km=0.068, diameter_m=0.15, k_mm=1, name="Pipe 10")
pipe11 = pp.create_pipe_from_parameters(net, from_junction=junction10, to_junction=junction11, length_km=0.17, diameter_m=0.25, k_mm=1, name="Pipe 11")
pipe12 = pp.create_pipe_from_parameters(net, from_junction=junction11, to_junction=junction12, length_km=0.108, diameter_m=0.25, k_mm=1, name="Pipe 12")
pipe13 = pp.create_pipe_from_parameters(net, from_junction=junction12, to_junction=junction13, length_km=0.106, diameter_m=0.15, k_mm=1, name="Pipe 13")
pipe14 = pp.create_pipe_from_parameters(net, from_junction=junction12, to_junction=junction14, length_km=0.172, diameter_m=0.2, k_mm=1, name="Pipe 14")
pipe15 = pp.create_pipe_from_parameters(net, from_junction=junction7, to_junction=junction13, length_km=0.240, diameter_m=0.15, k_mm=1, name="Pipe 15")


#sink for constant consumption. The sign of the mass flow is positive.
sink1 = pp.create_sink(net, junction=junction2, mdot_kg_per_s=0.0198, name="Sink 2")
sink2 = pp.create_sink(net, junction=junction3, mdot_kg_per_s=0.0423, name="Sink 3")
sink3 = pp.create_sink(net, junction=junction4, mdot_kg_per_s=0.0269, name="Sink 4")
sink4 = pp.create_sink(net, junction=junction5, mdot_kg_per_s=0.0165, name="Sink 5")
sink5 = pp.create_sink(net, junction=junction6, mdot_kg_per_s=0.0469, name="Sink 6")
sink6 = pp.create_sink(net, junction=junction7, mdot_kg_per_s=0.0497, name="Sink 7")
sink7 = pp.create_sink(net, junction=junction8, mdot_kg_per_s=0.0465, name="Sink 8")
sink8 = pp.create_sink(net, junction=junction9, mdot_kg_per_s=0.0539, name="Sink 9")
sink9 = pp.create_sink(net, junction=junction10, mdot_kg_per_s=0.0023, name="Sink 10")
sink10 = pp.create_sink(net, junction=junction11, mdot_kg_per_s=0.0453, name="Sink 11")
sink11 = pp.create_sink(net, junction=junction12, mdot_kg_per_s=0.0280, name="Sink 12")
sink12 = pp.create_sink(net, junction=junction13, mdot_kg_per_s=0.0603, name="Sink 13")
sink13 = pp.create_sink(net, junction=junction14, mdot_kg_per_s=0.0690, name="Sink 14")



#run pipeflow
#pp.pipeflow(net)
pp.pipeflow(net,friction_model="colebrook")
net.res_junction
print(net.res_junction)

#show junction table
print(net.junction)  
#print(net.source)
print(net.res_pipe)
#print(net.sink)
#net.res_sink
#print(net.res_sink)

    
# show full table
pd.set_option("display.max_rows", None, "display.max_columns", None)

#plotting
import pandapipes.plotting as plot
plot.simple_plot(net, plot_grid=True, plot_sinks=True, plot_sources=True, grid_size=2.0, sink_size=1.0, source_size=1.0)
