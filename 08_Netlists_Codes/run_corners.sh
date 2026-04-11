#!/bin/bash

echo "Running corner: TT (Typical)"
ngspice -b meminductor_tt.cir > corner_tt_new.txt

echo "Running corner: FF (Fast-Fast)"
ngspice -b meminductor_ff.cir > corner_ff_new.txt

echo "Running corner: SS (Slow-Slow)"
ngspice -b meminductor_ss.cir > corner_ss_new.txt

echo "Running corner: FS (Fast-Slow)"
ngspice -b meminductor_fs.cir > corner_fs_new.txt

echo "Running corner: SF (Slow-Fast)"
ngspice -b meminductor_sf.cir > corner_sf_new.txt

echo "All corners completed"
