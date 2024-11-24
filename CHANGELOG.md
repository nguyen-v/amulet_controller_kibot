# Changelog

## [Unreleased]

### Fixed

-   Replace non-stocked components.

## [1.1] - 2024-04-13

### Added

-   RC snubber passive values.

### Fixed

-   More vias for VBUS and LMR36006 GND pads.
-   Board version voltage reference from +3V3 to +A3V3.

### Changed

-   Motor thermistor resistor divider to 2kOhm for a 10k 3950K thermistor.

### Removed

## [1.0.2] - 2024-03-12

### Changed

-   Power sequencing graph according to experimental data.

## [1.0.1] - 2024-01-25

### Added

-   Controller target specifications.
-   Credits to moteus on cover page.
-   Optional RC-Snubber to power stage.

### Fixed

-   Chassis guard ring to go around the board.
-   CAN and power TVS diodes now go to chassis.
-   Clearance between nets to respect IEC60664-1 where possible.
-   Comment on precharge.
-   Power TVS diode reference designator from "U" to "D".

### Changed

-   5V 300 mA buck converter with 600 mA version.
-   Chassis-GND capacitor by 1nF 1kV.

## [1.0.0] - 2023-12-12

### Added

-   TVS protection and termination switch to FD-CAN.
-   Low-side switched 12V 600 mA source for external fan.
-   LDO for analog supply.
-   One TVS diode per power connector.
-   Second on-board I2C magnetic encoder for disambiguation.
-   ESD protection to all interfaces.
-   Over-voltage protection on thermistor ADC inputs.
-   Pi filters to inputs of buck regulators and MCU analog supply.
-   Decoupling caps next to power pins of connectors.

### Changed

-   CPH-CPL capacitor to 47 nF (gate driver).
-   FD-CAN transceiver IC.
-   FETs for top cooled variant.
-   Input power TVS diode to bidirectional.
-   Moved SOx low-pass filter to MCU section.
-   PWM_PHASEA with PWM_PHASEC on STM32G474 pinout for easier routing.
-   RS422 pinout on connector.
-   Buck regulators to optimize for low noise.

[Unreleased]: https://github.com/nguyen-v/amulet_controller_kibot/compare/1.2...HEAD

[1.2]: https://github.com/nguyen-v/amulet_controller_kibot/compare/993643f0a078ffdc2718bbcf903f86ae4c8dd2a2...1.2
