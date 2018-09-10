model;

set WELLS;
set FLASH_PLANTS;
set GENERATORS;

var open {WELLS} binary;
var flows_to {WELLS, FLASH_PLANTS} binary;

param mass_flow {WELLS} >= 0;
var lp_flow {WELLS} >= 0;
var ip_flow {WELLS} >= 0;
param well_enthalpy {WELLS};
var fp_enthalpy {FLASH_PLANTS} >= 0;

# enthalpy parameters
param hf_ip;
param hfg_ip;
param hf_lp;
param hfg_lp;


# calculations
s.t. fp_enthalpy {f in FLASH_PLANTS}:
	fp_enthalpy[f] <= sum {w in WELLS} mass_flow[w] * well_enthalpy[w] * flows_to[w, f]# / sum of 

s.t. ip_flow_calc {w in WELLS}:
	ip_flow[w] = (enthalpy[w] - hf_ip) / hfg_ip * mass_flow[w];

s.t. lp_flow_calc {w in WELLS}:
	lp_flow[w] = (hf_ip - hf_lp) / hfg_lp * (mass_flow[w] - ip_flow[w]);

s.t. w_flow_calc {w in WELLS}:
	
	

# limits
s.t. mass_draw:
	sum {w in WELLS} mass_flow[w] <= max_daily_draw;