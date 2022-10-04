odrv0.axis0.motor.config.requested_current_range = 200
odrv0.config.enable_brake_resistor = True

odrv0.axis0.motor.config.current_lim = 200
# odrv0.axis0.motor.config.pole_pairs = 3
odrv0.axis0.motor.config.pole_pairs = 11
odrv0.axis0.controller.config.vel_gain = 0.011
odrv0.axis0.controller.config.vel_integrator_gain = 0.05
odrv0.axis0.controller.config.control_mode = 2
# odrv0.axis0.sensorless_estimator.config.pm_flux_linkage = 5.51328895422 / (3 * 2100)
# TMotor
odrv0.axis0.sensorless_estimator.config.pm_flux_linkage = 5.51328895422 / (11 * 420)
odrv0.axis0.motor.config.requested_current_range = 200
odrv0.axis0.motor.config.current_lim_margin = 30
odrv0.axis0.motor.config.resistance_calib_max_voltage = 3.5
odrv0.axis0.motor.config.calibration_current = 30
odrv0.axis0.controller.config.vel_limit = 800
odrv0.axis0.config.enable_sensorless_mode = True

odrv0.axis1.motor.config.current_lim = 200
# odrv0.axis1.motor.config.pole_pairs = 3
odrv0.axis0.motor.config.pole_pairs = 11
odrv0.axis1.controller.config.vel_gain = 0.01
odrv0.axis1.controller.config.vel_integrator_gain = 0.05
odrv0.axis1.controller.config.control_mode = 2
# 5.51328895422 / (<pole pairs> * <KV>)
# odrv0.axis1.sensorless_estimator.config.pm_flux_linkage = 5.51328895422 / (3 * 2100)
# TMotor
odrv0.axis1.sensorless_estimator.config.pm_flux_linkage = 5.51328895422 / (11 * 420)
odrv0.axis1.motor.config.requested_current_range = 200
odrv0.axis1.motor.config.current_lim_margin = 30
odrv0.axis1.motor.config.resistance_calib_max_voltage = 3.5
odrv0.axis1.motor.config.calibration_current = 30
odrv0.axis1.controller.config.vel_limit = 800
odrv0.axis1.config.enable_sensorless_mode = True