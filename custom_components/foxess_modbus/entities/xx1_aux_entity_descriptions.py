"""Inverter sensor"""
import logging

from custom_components.foxess_modbus.entities.modbus_integration_sensor import (
    ModbusIntegrationSensorDescription,
)
from custom_components.foxess_modbus.entities.validation import Min
from custom_components.foxess_modbus.entities.validation import Range
from homeassistant.components.number import NumberDeviceClass
from homeassistant.components.number import NumberMode
from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.components.sensor import SensorStateClass
from homeassistant.const import UnitOfTime

from .entity_factory import EntityFactory
from .modbus_number import ModbusNumberDescription
from .modbus_select import ModbusSelectDescription
from .modbus_sensor import ModbusSensorDescription

_LOGGER: logging.Logger = logging.getLogger(__package__)

H1: list[EntityFactory] = [
    ModbusSensorDescription(
        key="pv1_voltage",
        addresses=[11000],
        name="PV1 Voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="V",
        scale=0.1,
        # This can go negative if no panels are attached
    ),
    ModbusSensorDescription(
        key="pv1_current",
        addresses=[11001],
        name="PV1 Current",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="A",
        scale=0.1,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="pv1_power",
        addresses=[11002],
        name="PV1 Power",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
        # This can go negative if no panels are attached
    ),
    ModbusIntegrationSensorDescription(
        key="pv1_energy_total",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        native_unit_of_measurement="kWh",
        integration_method="left",
        name="PV1 Power Total",
        round_digits=2,
        source_entity="pv1_power",
        unit_time=UnitOfTime.HOURS,
    ),
    ModbusSensorDescription(
        key="pv2_voltage",
        addresses=[11003],
        name="PV2 Voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="V",
        scale=0.1,
        # This can go negative if no panels are attached
    ),
    ModbusSensorDescription(
        key="pv2_current",
        addresses=[11004],
        name="PV2 Current",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="A",
        scale=0.1,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="pv2_power",
        addresses=[11005],
        name="PV2 Power",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
        # This can go negative if no panels are attached
    ),
    ModbusIntegrationSensorDescription(
        key="pv2_energy_total",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        native_unit_of_measurement="kWh",
        integration_method="left",
        name="PV2 Power Total",
        round_digits=2,
        source_entity="pv2_power",
        unit_time=UnitOfTime.HOURS,
    ),
]

AC1: list[EntityFactory] = []

H1_AC1: list[EntityFactory] = [
    ModbusSensorDescription(
        key="invbatvolt",
        addresses=[11006],
        name="Inverter Battery Voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="V",
        scale=0.1,
        # This can go negative if no battery is attached
    ),
    ModbusSensorDescription(
        key="invbatcurrent",
        addresses=[11007],
        name="Inverter Battery Current",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="A",
        scale=0.1,
        validate=[Range(-100, 100)],
    ),
    ModbusSensorDescription(
        key="invbatpower",
        addresses=[11008],
        name="Inverter Battery Power",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
        validate=[Range(-10000, 10000)],
    ),
    ModbusSensorDescription(
        key="battery_discharge",
        addresses=[11008],
        name="Battery Discharge",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
        post_process=lambda v: v if v > 0 else 0,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="battery_charge",
        addresses=[11008],
        name="Battery Charge",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
        post_process=lambda v: abs(v) if v < 0 else 0,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="rvolt",
        addresses=[11009],
        name="Inverter Voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="V",
        scale=0.1,
        validate=[Range(0, 300)],
    ),
    ModbusSensorDescription(
        key="rcurrent",
        addresses=[11010],
        name="Inverter Current",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="A",
        scale=0.1,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="rpower",
        addresses=[11011],
        name="Inverter Power",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
        validate=[Range(-10000, 10000)],
    ),
    ModbusSensorDescription(
        key="rfreq",
        addresses=[11014],
        name="Inverter Frequency",
        device_class=SensorDeviceClass.FREQUENCY,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="Hz",
        scale=0.01,
        validate=[Range(0, 60)],
    ),
    ModbusSensorDescription(
        key="eps_rvolt",
        addresses=[11015],
        name="EPS Voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="V",
        scale=0.1,
        validate=[Range(0, 300)],
    ),
    ModbusSensorDescription(
        key="grid_ct",
        addresses=[11021],
        name="Grid CT",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
        validate=[Range(-100, 100)],
    ),
    ModbusSensorDescription(
        key="feed_in",
        addresses=[11021],
        name="Feed-in",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
        post_process=lambda v: v if v > 0 else 0,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="grid_consumption",
        addresses=[11021],
        name="Grid Consumption",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
        post_process=lambda v: abs(v) if v < 0 else 0,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="ct2_meter",
        addresses=[11022],
        name="CT2 Meter",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
        validate=[Range(-100, 100)],
    ),
    ModbusSensorDescription(
        key="load_power",
        addresses=[11023],
        name="Load Power",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
        validate=[Range(-100, 100)],
    ),
    ModbusIntegrationSensorDescription(
        key="load_power_total",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        native_unit_of_measurement="kWh",
        integration_method="left",
        name="Load Power Total",
        round_digits=2,
        source_entity="load_power",
        unit_time=UnitOfTime.HOURS,
    ),
    ModbusSensorDescription(
        key="invtemp",
        addresses=[11024],
        name="Inverter Temp",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="°C",
        scale=0.1,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="ambtemp",
        addresses=[11025],
        name="Ambient Temp",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="°C",
        scale=0.1,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="batvolt",
        addresses=[11034],
        name="Battery Voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="V",
        scale=0.1,
        validate=[Min(0)],
    ),
    ModbusSensorDescription(
        key="bat_current",
        addresses=[11035],
        name="Battery Current",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="A",
        scale=0.1,
        validate=[Range(-100, 100)],
    ),
    ModbusSensorDescription(
        key="battery_soc",
        addresses=[11036],
        name="Battery SoC",
        device_class=SensorDeviceClass.BATTERY,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="%",
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="bms_kwh_remaining",
        addresses=[11037],
        name="BMS kWh Remaining",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        native_unit_of_measurement="kWh",
        scale=0.01,
        validate=[Min(0)],
    ),
    ModbusSensorDescription(
        key="battery_temp",
        addresses=[11038],
        name="Battery Temp",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="°C",
        scale=0.1,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="bms_charge_rate",
        addresses=[11041],
        name="BMS Charge Rate",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="A",
        scale=0.1,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="bms_discharge_rate",
        addresses=[11042],
        name="BMS Discharge Rate",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="A",
        scale=0.1,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="bms_cell_temp_high",
        addresses=[11043],
        name="BMS Cell Temp High",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="°C",
        scale=0.1,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="bms_cell_temp_low",
        addresses=[11044],
        name="BMS Cell Temp Low",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="°C",
        scale=0.1,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="bms_cell_mv_high",
        addresses=[11045],
        name="BMS Cell mV High",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="mV",
        validate=[Min(0)],
    ),
    ModbusSensorDescription(
        key="bms_cell_mv_low",
        addresses=[11046],
        name="BMS Cell mV Low",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="mV",
        validate=[Min(0)],
    ),
    ModbusSensorDescription(
        key="bms_cycle_count",
        addresses=[11048],
        name="BMS Cycle Count",
        state_class=SensorStateClass.MEASUREMENT,
        validate=[Min(0)],
    ),
    ModbusSensorDescription(
        key="bms_watthours_total",
        addresses=[11049],
        name="BMS Watthours Total",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        native_unit_of_measurement="kWh",
        scale=0.1,
        signed=False,
        validate=[Min(0)],
    ),
    ModbusSensorDescription(
        key="solar_energy_total",
        addresses=[11070, 11069],
        name="Solar Generation Total",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        native_unit_of_measurement="kWh",
        scale=0.1,
        signed=False,
        validate=[Min(0)],
    ),
    ModbusSensorDescription(
        key="solar_energy_today",
        addresses=[11071],
        name="Solar Generation Today",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        native_unit_of_measurement="kWh",
        scale=0.1,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="battery_charge_total",
        addresses=[11073, 11072],
        name="Battery Charge Total",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        native_unit_of_measurement="kWh",
        scale=0.1,
        signed=False,
        validate=[Min(0)],
    ),
    ModbusSensorDescription(
        key="battery_charge_today",
        addresses=[11074],
        name="Battery Charge Today",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        native_unit_of_measurement="kWh",
        scale=0.1,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="battery_discharge_total",
        addresses=[11076, 11075],
        name="Battery Discharge Total",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        native_unit_of_measurement="kWh",
        scale=0.1,
        signed=False,
        validate=[Min(0)],
    ),
    ModbusSensorDescription(
        key="battery_discharge_today",
        addresses=[11077],
        name="Battery Discharge Today",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        native_unit_of_measurement="kWh",
        scale=0.1,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="feed_in_energy_total",
        addresses=[11079, 11078],
        name="Feed-in Total",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        native_unit_of_measurement="kWh",
        scale=0.1,
        signed=False,
        validate=[Min(0)],
    ),
    ModbusSensorDescription(
        key="feed_in_energy_today",
        addresses=[11080],
        name="Feed-in Today",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        native_unit_of_measurement="kWh",
        scale=0.1,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="grid_consumption_energy_total",
        addresses=[11082, 11081],
        name="Grid Consumption Total",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        native_unit_of_measurement="kWh",
        scale=0.1,
        signed=False,
        validate=[Min(0)],
    ),
    ModbusSensorDescription(
        key="grid_consumption_energy_today",
        addresses=[11083],
        name="Grid Consumption Today",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        native_unit_of_measurement="kWh",
        scale=0.1,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="total_yield_total",
        addresses=[11085, 11084],
        name="Yield Total",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        native_unit_of_measurement="kWh",
        scale=0.1,
        signed=False,
        validate=[Min(0)],
    ),
    ModbusSensorDescription(
        key="total_yield_today",
        addresses=[11086],
        name="Yield Today",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        native_unit_of_measurement="kWh",
        scale=0.1,
        # unsure if this actually goes negative
        validate=[Range(-100, 100)],
    ),
    ModbusSelectDescription(
        key="work_mode",
        address=41000,
        name="Work Mode",
        options_map={0: "Self Use", 1: "Feed-in First", 2: "Back-up"},
    ),
    # Sensor kept for back compat
    ModbusSensorDescription(
        key="min_soc",
        addresses=[41009],
        name="Min SoC",
        device_class=SensorDeviceClass.BATTERY,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="%",
        validate=[Range(0, 100)],
    ),
    ModbusNumberDescription(
        key="min_soc",
        address=41009,
        name="Min SoC",
        mode=NumberMode.BOX,
        native_min_value=10,
        native_max_value=100,
        native_step=1,
        native_unit_of_measurement="%",
        device_class=NumberDeviceClass.BATTERY,
        icon="mdi:battery-arrow-down",
        validate=[Range(0, 100)],
    ),
    # Sensor kept for back compat
    ModbusSensorDescription(
        key="max_soc",
        addresses=[41010],
        name="Max SoC",
        device_class=SensorDeviceClass.BATTERY,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="%",
        validate=[Range(0, 100)],
    ),
    ModbusNumberDescription(
        key="max_soc",
        address=41010,
        name="Max SoC",
        mode=NumberMode.BOX,
        native_min_value=10,
        native_max_value=100,
        native_step=1,
        native_unit_of_measurement="%",
        device_class=NumberDeviceClass.BATTERY,
        icon="mdi:battery-arrow-up",
        validate=[Range(0, 100)],
    ),
    # Sensor kept for back compat
    ModbusSensorDescription(
        key="min_soc_on_grid",
        addresses=[41011],
        name="Min SoC (On Grid)",
        device_class=SensorDeviceClass.BATTERY,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="%",
        validate=[Range(0, 100)],
    ),
    ModbusNumberDescription(
        key="min_soc_on_grid",
        address=41011,
        name="Min SoC (On Grid)",
        mode=NumberMode.BOX,
        native_min_value=10,
        native_max_value=100,
        native_step=1,
        native_unit_of_measurement="%",
        device_class=NumberDeviceClass.BATTERY,
        icon="mdi:battery-arrow-down",
        validate=[Range(0, 100)],
    ),
]
