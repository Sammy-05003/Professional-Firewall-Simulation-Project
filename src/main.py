#!/usr/bin/env python3
from firewall import Firewall
from rules_manager import RulesManager
from packet import Packet
from cli import FirewallCLI

def main():
    # Initialize components
    rules_manager = RulesManager()
    firewall = Firewall(rules_manager)
    cli = FirewallCLI(firewall)
    
    # Start the CLI interface
    cli.start()

if __name__ == "__main__":
    main()