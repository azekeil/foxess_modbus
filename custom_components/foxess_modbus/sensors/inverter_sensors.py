"""Inverter sensor"""
import logging
from datetime import time

from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.components.sensor import SensorStateClass

from .modbus_sensor import ModbusSensor
from .sensor_desc import SensorDescription

_LOGGER: logging.Logger = logging.getLogger(__package__)

SENSORS: dict[str, SensorDescription] = {
    "pv1-voltage": SensorDescription(
        key="pv1-voltage",
        address=11000,
        name="PV1 Voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="V",
        post_process=lambda v: v / 10,
    ),
    "pv1-current": SensorDescription(
        key="pv1-current",
        address=11001,
        name="PV1 Current",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="A",
        post_process=lambda v: v / 10,
    ),
    "pv1-power": SensorDescription(
        key="pv1-power",
        address=11002,
        name="PV1 Power",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        post_process=lambda v: v / 1000,
    ),
    "pv2-voltage": SensorDescription(
        key="pv2-voltage",
        address=11003,
        name="PV2 Voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="V",
        post_process=lambda v: v / 10,
    ),
    "pv2-current": SensorDescription(
        key="pv2-current",
        address=11004,
        name="PV2 Current",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="A",
        post_process=lambda v: v / 10,
    ),
    "pv2-power": SensorDescription(
        key="pv2-power",
        address=11005,
        name="PV2 Power",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        post_process=lambda v: v / 1000,
    ),
    "battery-soc": SensorDescription(
        key="battery-soc",
        address=11036,
        name="Battery SoC",
        device_class=SensorDeviceClass.BATTERY,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="%",
    ),
    "battery-discharge": SensorDescription(
        key="battery-discharge",
        address=11008,
        name="Battery Discharge",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        post_process=lambda v: v / 1000 if v > 0 else 0,
    ),
    "battery-charge": SensorDescription(
        key="battery-charge",
        address=11008,
        name="Battery Charge",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        post_process=lambda v: abs(v) / 1000 if v < 0 else 0,
    ),
    "feed-in": SensorDescription(
        key="feed-in",
        address=11021,
        name="Feed In",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        post_process=lambda v: v / 1000 if v > 0 else 0,
    ),
    "grid-consumption": SensorDescription(
        key="grid-consumption",
        address=11021,
        name="Grid Consumption",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        post_process=lambda v: abs(v) / 1000 if v < 0 else 0,
    ),
    "battery-temp": SensorDescription(
        key="battery-temp",
        address=11038,
        name="Battery Temp",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="°C",
        post_process=lambda v: v / 10,
    ),
    "inv-temp": SensorDescription(
        key="inv-temp",
        address=11024,
        name="Inverter Temp",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="°C",
        post_process=lambda v: v / 10,
    ),
    "amb-temp": SensorDescription(
        key="amb-temp",
        address=11025,
        name="Ambient Temp",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="°C",
        post_process=lambda v: v / 10,
    ),
    "load-power": SensorDescription(
        key="load-power",
        address=11023,
        name="Load Power",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        post_process=lambda v: v / 1000,
    ),
    "inv-bat-volt": SensorDescription(
        key="inv-bat-volt",
        address=11006,
        name="Load Power",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="V",
        post_process=lambda v: v / 10,
    ),
    "inv-bat-power": SensorDescription(
        key="inv-bat-power",
        address=11007,
        name="Load Power",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        post_process=lambda v: v / 100,
    ),
    "grid-ct": SensorDescription(
        key="grid-ct",
        address=11021,
        name="Grid CT",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        post_process=lambda v: v / 1000,
    ),
    "bat-voltage": SensorDescription(
        key="bat-voltage",
        address=11034,
        name="Battery Voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="V",
        post_process=lambda v: v / 10,
    ),
    "min-soc": SensorDescription(
        key="min-soc",
        address=41009,
        name="Min SoC",
        device_class=SensorDeviceClass.BATTERY,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="%",
    ),
    "min-soc-grid": SensorDescription(
        key="min-soc-grid",
        address=41011,
        name="Min SoC (On Grid)",
        device_class=SensorDeviceClass.BATTERY,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="%",
    ),
    "period1-enabled": SensorDescription(
        key="period1-enabled",
        address=41001,
        name="Period 1 - Enabled",
        post_process=lambda v: bool(v),
    ),
    "period1-start": SensorDescription(
        key="period1-start",
        address=41002,
        name="Period 1 - Start",
        post_process=lambda v: time(hour=(v // 256), minute=v - ((v // 256) * 256)),
    ),
    "period1-end": SensorDescription(
        key="period1-end",
        address=41003,
        name="Period 1 - End",
        post_process=lambda v: time(hour=(v // 256), minute=v - ((v // 256) * 256)),
    ),
    "period2-enabled": SensorDescription(
        key="period2-enabled",
        address=41004,
        name="Period 2 - Enabled",
        post_process=lambda v: bool(v),
    ),
    "period2-start": SensorDescription(
        key="period2-start",
        address=41005,
        name="Period 2 - Start",
        post_process=lambda v: time(hour=(v // 256), minute=v - ((v // 256) * 256)),
    ),
    "period2-end": SensorDescription(
        key="period2-end",
        address=41006,
        name="Period 2 - End",
        post_process=lambda v: time(hour=(v // 256), minute=v - ((v // 256) * 256)),
    ),
    "bms-cell-voltage-high": SensorDescription(
        key="bms-cell-voltage-high",
        address=11045,
        name="BMS Cell mV High",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="mV",
    ),
    "bms-cell-voltage-low": SensorDescription(
        key="bms-cell-voltage-low",
        address=11046,
        name="BMS Cell mV Low",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="mV",
    ),
    "bms-charge-rate": SensorDescription(
        key="bms-charge-rate",
        address=11041,
        name="BMS Charge Rate",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="A",
        post_process=lambda v: v / 10,
    ),
    "bms-discharge-rate": SensorDescription(
        key="bms-discharge-rate",
        address=11042,
        name="BMS Discharge Rate",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="A",
        post_process=lambda v: v / 10,
    ),
    "bms-cell-temp-high": SensorDescription(
        key="bms-cell-temp-high",
        address=11043,
        name="BMS Cell Temp High",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="°C",
        post_process=lambda v: v / 10,
    ),
    "bms-cell-temp-low": SensorDescription(
        key="bms-cell-temp-low",
        address=11044,
        name="BMS Cell Temp Low",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="°C",
        post_process=lambda v: v / 10,
    ),
    "bms-kw-remaining": SensorDescription(
        key="bms-kw-remaining",
        address=11037,
        name="BMS kW Remaining",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kWh",
        post_process=lambda v: v / 100,
    ),
}


def sensors(controllers, entry) -> list:
    """Setup sensor platform."""
    entities = []

    for sensor in SENSORS:
        sen = ModbusSensor(controllers["modbus"], SENSORS[sensor], entry)
        entities.append(sen)

    return entities
