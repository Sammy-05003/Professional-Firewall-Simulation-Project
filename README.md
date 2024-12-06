# Professional Firewall Simulation

A sophisticated rule-based firewall simulation that demonstrates network security concepts and professional software development practices.

## Features

- Rule-based packet filtering
- Support for IP address, port, and protocol filtering
- Wildcard matching support
- Comprehensive logging system
- Interactive CLI interface
- Unit tests
- Professional error handling
- Persistent rule storage

## Technical Highlights

- Clean Architecture
- Object-Oriented Design
- Type Hints
- Comprehensive Error Handling
- Unit Testing
- Logging System
- Data Persistence
- Command Pattern (CLI)
- Input Validation

## Usage

1. Start the firewall simulator:
   ```
   python src/main.py
   ```

2. Available Commands:
   - `add_rule <ip_address> <port> <protocol> <action>`: Add a new firewall rule
   - `list_rules`: Display all current rules
   - `remove_rule <index>`: Remove a rule by its index
   - `test_packet <ip_address> <port> <protocol>`: Test if a packet would be allowed
   - `quit`: Exit the simulator

## Example Usage

```bash
# Add a rule to block TCP traffic to port 80 from a specific IP
add_rule 192.168.1.100 80 TCP BLOCK

# Add a rule to allow all UDP traffic from a subnet
add_rule 10.0.0.* * UDP ALLOW

# Test a packet
test_packet 192.168.1.100 80 TCP

# List all rules
list_rules
```

## Project Structure

```
firewall-simulation/
├── src/
│   ├── main.py          # Entry point
│   ├── firewall.py      # Core firewall logic
│   ├── rules_manager.py # Rule management
│   ├── packet.py        # Packet data structure
│   └── cli.py           # Command-line interface
├── tests/
│   └── test_firewall.py # Unit tests
└── README.md            # Documentation
```

## Skills Demonstrated

- Python Programming
- Network Security Concepts
- Software Architecture
- Object-Oriented Design
- Testing Methodologies
- Error Handling
- Input Validation
- Documentation