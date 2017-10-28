import physical_validation as pv
import os

systems_nvt = [
    'ens_water_md_verlet_settle_pme_vr',
    'ens_water_md_verlet_settle_pme_be'
]
systems_npt = [
    'ens_water_md_verlet_settle_pme_vr_pr',
    'ens_water_md_verlet_settle_pme_be_pr'
]

parser = pv.data.FlatfileParser()

topology = pv.data.TopologyData(
    natoms=900*3,
    nconstraints=900*3,
    ndof_reduction_tra=3,
    ndof_reduction_rot=0
)

units = pv.data.UnitData(
    kb=8.314462435405199e-3,
    energy_str='kJ/mol',
    energy_conversion=1.0,
    length_str='nm',
    length_conversion=1.0,
    volume_str='nm^3',
    volume_conversion=1.0,
    pressure_str='bar',
    pressure_conversion=1.0,
    time_str='ps',
    time_conversion=1.0
)

nvt_low = pv.data.EnsembleData(
    ensemble='NVT',
    natoms=900*3,
    volume=3.01125**3,
    temperature=298.15
)
nvt_high = pv.data.EnsembleData(
    ensemble='NVT',
    natoms=900*3,
    volume=3.01125**3,
    temperature=308.15
)

npt_low = pv.data.EnsembleData(
    ensemble='NPT',
    natoms=900*3,
    pressure=1.0,
    temperature=298.15
)
npt_high = pv.data.EnsembleData(
    ensemble='NPT',
    natoms=900*3,
    pressure=101.0,
    temperature=308.15
)

for sys in systems_nvt + systems_npt:
    print('### Analyzing system ' + sys)
    print('## Reading lower temperature result')
    dir_low = os.path.join(sys, 'base', 'run')
    if sys in systems_nvt:
        res_low = parser.get_simulation_data(
            units=units, ensemble=nvt_low, topology=topology,
            kinetic_ene_file=os.path.join(dir_low, 'kinetic.dat'),
            potential_ene_file=os.path.join(dir_low, 'potential.dat'),
            total_ene_file=os.path.join(dir_low, 'total.dat')
        )
    else:
        res_low = parser.get_simulation_data(
            units=units, ensemble=npt_low, topology=topology,
            kinetic_ene_file=os.path.join(dir_low, 'kinetic.dat'),
            potential_ene_file=os.path.join(dir_low, 'potential.dat'),
            total_ene_file=os.path.join(dir_low, 'total.dat'),
            pressure_file=os.path.join(dir_low, 'pressure.dat'),
            volume_file=os.path.join(dir_low, 'volume.dat')
        )
    print('## Reading high temperature result')
    dir_high = os.path.join(sys, 'ensemble_1', 'run')
    if sys in systems_nvt:
        res_high = parser.get_simulation_data(
            units=units, ensemble=nvt_high, topology=topology,
            kinetic_ene_file=os.path.join(dir_high, 'kinetic.dat'),
            potential_ene_file=os.path.join(dir_high, 'potential.dat'),
            total_ene_file=os.path.join(dir_high, 'total.dat')
        )
    else:
        res_high = parser.get_simulation_data(
            units=units, ensemble=npt_high, topology=topology,
            kinetic_ene_file=os.path.join(dir_high, 'kinetic.dat'),
            potential_ene_file=os.path.join(dir_high, 'potential.dat'),
            total_ene_file=os.path.join(dir_high, 'total.dat'),
            pressure_file=os.path.join(dir_high, 'pressure.dat'),
            volume_file=os.path.join(dir_high, 'volume.dat')
        )

    if not os.path.exists('ana_water_plots'):
        os.makedirs('ana_water_plots')
    sysplot = os.path.join('ana_water_plots', sys)
    print('\n## Validating kinetic energy distribution (alpha = 0.05)')
    alpha = 0.05
    print('# Low T:')
    pv.kinetic_energy.mb_ensemble(res_low, alpha=alpha, verbose=True,
                                  screen=False, filename=sysplot + '_low_mb')
    print('# High T:')
    pv.kinetic_energy.mb_ensemble(res_high, alpha=alpha, verbose=True,
                                  screen=False, filename=sysplot + '_high_mb')
    print('\n## Validating ensemble')
    quantiles = pv.ensemble.check(res_low, res_high, quiet=False,
                                  screen=False, filename=sysplot + '_ensemble')
    if len(quantiles) == 1:
        q_str = '{:.1f}'.format(quantiles[0])
    else:
        q_str = '('
        for q in quantiles:
            q_str += '{:.1f}, '.format(q)
        q_str = q_str[:-2] + ')'
    print('Calculated slope is ' + q_str +
          ' quantiles from the true slope')
    print('\n')
