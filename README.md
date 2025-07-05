Salt Corrector app

A simple GUI-based salt correction calculator for food industry use.  
Written in **Python** using **CustomTkinter**, this tool helps determine the necessary amount of a correcting component (with higher or lower salt content) to adjust the salt level of a batch that is outside the acceptable range.

Purpose

In food production, it's common to encounter batches with salt levels outside the desired specification. This calculator assists in adjusting the salt concentration by:
- Adding a more salty material to **increase** the salt level.
- Adding a less salty (diluting) material to **decrease** the salt level.

How it works

The user inputs:
- Multiple measured salt values from the current batch (separated with space)
- The batch size (in kilograms).
- The target salt percentage.
- The salt percentage of the correcting component.

The program calculates:
- The average measured salt percentage.
- The required quantity of correcting material.
- The new total batch size after correction.

GUI Layout

The interface includes the following fields:

| Field | Description |
|-------|-------------|
| **Measured Salt** | Space-separated list of salt measurements from the batch |
| **Batch Size** | Total mass of the original batch in kg |
| **Target Salt** | The desired salt concentration (%) |
| **Component Salt** | Salt concentration (%) of the correcting material |
| **QTY** | Calculated quantity of the correcting material to add (kg) |
| **NEW SIZE** | Final batch size after correction (kg) |

A **"Calculate"** button triggers the computation.



Installation & Requirements

This script requires Python and the [`customtkinter`](https://github.com/TomSchimansky/CustomTkinter) library.

Install dependencies via pip:
bash
pip install customtkinter
