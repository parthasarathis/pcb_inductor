
# PCB Inductor Design Tool

Welcome to the PCB Inductor Design Tool! This open-source tool simplifies the design of different shapes of PCB inductors, including square, hexagonal, and octagonal shapes. The tool allows you to input desired dimensions and shapes and automatically performs necessary calculations for designing PCB inductors.

## Features

- **Inductor Design**: The tool helps design inductors of different shapes, including square, hexagonal, and octagonal.
- **Calculation of Inductance**: The tool calculates the inductance of the designed inductor based on given parameters.
- **Integration with KiCad**: The tool can generate coordinates compatible with the KiCad PCB design software, enabling seamless integration.
- **User Input**: The tool accepts user inputs such as center coordinates, layer, track width, clearance, number of turns, shape selection, and more.

## Requirements

- Python 3.x

## Installation

1. Clone this repository:

    ```shell
    git clone https://github.com/yourusername/pcb-inductor-design-tool.git
    ```

2. Navigate to the project directory:

    ```shell
    cd pcb-inductor-design-tool
    ```

3. Run the script:

    ```shell
    python pcb_inductor_design_tool.py
    ```

## Usage

1. Upon running the script, you will be prompted to select the shape of the inductor:
    - Enter `1` for Square.
    - Enter `2` for Octagon.
    - Enter `3` for Hexagon.

2. You will be prompted to enter the relevant parameters for the chosen shape:
    - Track width in mm.
    - Clearance in mm.
    - Number of turns.

3. The tool will calculate the average diameter of the coil and its inductance.

4. The tool then continues to guide you through the design process:
    - Input center coordinates for the inductor.
    - Select the layer (`1` for Top Layer, `2` for Bottom Layer).
    - Specify the starting angle in degrees.
    - Choose the direction of rotation (`+1` for anticlockwise, `-1` for clockwise).

5. The tool will print out the coordinates for designing the inductor.

## Contribution

Contributions to this project are welcome! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b new-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin new-branch`).
6. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any issues, questions, or suggestions, please open an issue on the GitHub repository.

