# AICHE_workshop_2017
2017 AICHE Hands On Molecular Simulation Workshop

This repository contains 4 directories.

* Q1_structures/
	+ Q1_numbers/
		+ Q1_bad_structure.gro
		+ dump.txt
	+ Q1_pictures/
	 	+ Q1_data.xvg
         	+ Q1_structure.gro
         	+ Q1_unitcell.png

 * physical_validation/
	+ gmx_water/
	        + ana_waters.py  
		+ ens_water_md_verlet_settle_pme_be_pr/	
		+ ens_water_md_verlet_settle_pme_vr_pr/
		+ ens_water_md_verlet_settle_pme_be/	
		+ ens_water_md_verlet_settle_pme_vr/	    
	+ flat_water/
	        + ana_waters.py  
		+ ens_water_md_verlet_settle_pme_be_pr/	
		+ ens_water_md_verlet_settle_pme_vr_pr/
		+ ens_water_md_verlet_settle_pme_be/	
		+ ens_water_md_verlet_settle_pme_vr/	                

The scripts in `physical_validation` require cloning https://github.com/shirtsgroup/physical-validation and running `python setup.py. install` in the main repository.

  * heat_capacity/
     + calc_cv.py
     + isobutane_220K_1.xvg
     + isobutane_220K_2.xvg
     + isobutane_230K_1.xvg
     + isobutane_230K_2.xvg

  * bootstrap/
      + bootstraptest.py	
