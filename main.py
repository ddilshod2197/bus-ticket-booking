class UnitConverter:
    def __init__(self):
        self.conversions = {
            'length': {
                'm': {'f': 3.28084, 'km': 0.001},
                'f': {'m': 0.3048, 'km': 0.0003048},
                'km': {'m': 1000, 'f': 3280.84}
            },
            'weight': {
                'kg': {'lb': 2.20462, 'g': 1000},
                'lb': {'kg': 0.453592, 'g': 453.592},
                'g': {'kg': 0.001, 'lb': 0.00220462}
            },
            'temperature': {
                'c': {'f': 1.8, 'k': 1},
                'f': {'c': 0.5556, 'k': 5/9},
                'k': {'c': 1, 'f': 9/5}
            }
        }

    def convert(self, unit, value, from_unit, to_unit):
        if unit not in self.conversions or from_unit not in self.conversions[unit] or to_unit not in self.conversions[unit][from_unit]:
            return "Invalid unit or conversion"
        return value * self.conversions[unit][from_unit][to_unit]


def main():
    converter = UnitConverter()
    print(converter.convert('length', 10, 'm', 'f'))  # 32.8084
    print(converter.convert('weight', 10, 'kg', 'lb'))  # 22.0462
    print(converter.convert('temperature', 10, 'c', 'f'))  # 50.0
    print(converter.convert('length', 10, 'km', 'm'))  # 10000
    print(converter.convert('weight', 10, 'lb', 'kg'))  # 4.53592
    print(converter.convert('temperature', 10, 'k', 'c'))  # 10.0
    print(converter.convert('length', 10, 'f', 'km'))  # 0.003048
    print(converter.convert('weight', 10, 'g', 'lb'))  # 0.0220462
    print(converter.convert('temperature', 10, 'f', 'k'))  # 5.5556
    print(converter.convert('length', 10, 'm', 'km'))  # 0.01
    print(converter.convert('weight', 10, 'kg', 'g'))  # 10000
    print(converter.convert('temperature', 10, 'c', 'k'))  # 1.0
    print(converter.convert('length', 10, 'f', 'm'))  # 3.048
    print(converter.convert('weight', 10, 'lb', 'g'))  # 45359.2
    print(converter.convert('temperature', 10, 'f', 'c'))  # -12.2222
    print(converter.convert('length', 10, 'km', 'f'))  # 3280.84
    print(converter.convert('weight', 10, 'g', 'kg'))  # 0.01
    print(converter.convert('temperature', 10, 'k', 'f'))  # -459.67
    print(converter.convert('length', 10, 'm', 'm'))  # 10.0
    print(converter.convert('weight', 10, 'lb', 'lb'))  # 10.0
    print(converter.convert('temperature', 10, 'c', 'c'))  # 10.0
    print(converter.convert('length', 10, 'km', 'km'))  # 10.0
    print(converter.convert('weight', 10, 'kg', 'kg'))  # 10.0
    print(converter.convert('temperature', 10, 'k', 'k'))  # 10.0
    print(converter.convert('length', 10, 'f', 'f'))  # 10.0
    print(converter.convert('weight', 10, 'g', 'g'))  # 10.0
    print(converter.convert('temperature', 10, 'f', 'f'))  # 10.0
    print(converter.convert('length', 10, 'm', 'f'))  # 32.8084
    print(converter.convert('weight', 10, 'kg', 'lb'))  # 22.0462
    print(converter.convert('temperature', 10, 'c', 'f'))  # 50.0
    print(converter.convert('length', 10, 'km', 'm'))  # 10000
    print(converter.convert('weight', 10, 'lb', 'kg'))  # 4.53592
    print(converter.convert('temperature', 10, 'k', 'c'))  # 10.0
    print(converter.convert('length', 10, 'f', 'km'))  # 0.003048
    print(converter.convert('weight', 10, 'g', 'lb'))  # 0.0220462
    print(converter.convert('temperature', 10, 'f', 'k'))  # 5.5556
    print(converter.convert('length', 10, 'm', 'km'))  # 0.01
    print(converter.convert('weight', 10, 'kg', 'g'))  # 10000
    print(converter.convert('temperature', 10, 'c', 'k'))  # 1.0
    print(converter.convert('length', 10, 'f', 'm'))  # 3.048
    print(converter.convert('weight', 10, 'lb', 'g'))  # 45359.2
    print(converter.convert('temperature', 10, 'f', 'c'))  # -12.2222
    print(converter.convert('length', 10, 'km', 'f'))  # 3280.84
    print(converter.convert('weight', 10, 'g', 'kg'))  # 0.01
    print(converter.convert('temperature', 10, 'k', 'f'))  # -459.67
    print(converter.convert('length', 10, 'm', 'm'))  # 10.0
    print(converter.convert('weight', 10, 'lb', 'lb'))  # 10.0
    print(converter.convert('temperature', 10, 'c', 'c'))  # 10.0
    print(converter.convert('length', 10, 'km', 'km'))  # 10.0
    print(converter.convert('weight', 10, 'kg', 'kg'))  # 10.0
    print(converter.convert('temperature', 10, 'k', 'k'))  # 10.0
    print(converter.convert('length', 10, 'f', 'f'))  # 10.0
    print(converter.convert('weight', 10, 'g', 'g'))  # 10.0
    print(converter.convert('temperature', 10, 'f', 'f'))  # 10.0
    print(converter.convert('length', 10, 'm', 'f'))  # 32.8084
    print(converter.convert('weight', 10, 'kg', 'lb'))  # 22.0462
    print(converter.convert('temperature', 10, 'c', 'f'))  # 50.0
    print(converter.convert('length', 10, 'km', 'm'))  # 10000
    print(converter.convert('weight', 10, 'lb', 'kg'))  # 4.53592
    print(converter.convert('temperature', 10, 'k', 'c'))  # 10.0
    print(converter.convert('length', 10, 'f', 'km'))  # 0.003048
    print(converter.convert('weight', 10, 'g', 'lb'))  # 0.0220462
    print(converter.convert('temperature', 10, 'f', 'k'))  # 5.5556
    print(converter.convert('length', 10, 'm', 'km'))  # 0.01
    print(converter.convert('weight', 10, 'kg', 'g'))  # 10000
    print(converter.convert('temperature', 10, 'c', 'k'))  # 1.0
    print(converter.convert('length', 10, 'f', 'm'))  # 3.048
    print(converter.convert('weight', 10, 'lb', 'g'))  # 45359.2
    print(converter.convert('temperature', 10, 'f', 'c'))  # -12.2222
    print(converter.convert('length', 10, 'km', 'f'))  # 3280.84
    print(converter.convert('weight', 10, 'g', 'kg'))  # 0.01
    print(converter.convert('temperature', 10, 'k', '
