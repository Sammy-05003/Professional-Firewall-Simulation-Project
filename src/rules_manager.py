from dataclasses import dataclass
from typing import List
import json
import os

@dataclass
class FirewallRule:
    ip_address: str
    port: str
    protocol: str
    action: str  # "ALLOW" or "BLOCK"

class RulesManager:
    def __init__(self):
        self.rules: List[FirewallRule] = []
        self.rules_file = "firewall_rules.json"
        self.load_rules()
    
    def add_rule(self, ip_address: str, port: str, protocol: str, action: str) -> None:
        """Add a new firewall rule"""
        rule = FirewallRule(ip_address, port, protocol, action.upper())
        self.rules.append(rule)
        self.save_rules()
    
    def remove_rule(self, index: int) -> bool:
        """Remove a rule by index"""
        if 0 <= index < len(self.rules):
            self.rules.pop(index)
            self.save_rules()
            return True
        return False
    
    def get_rules(self) -> List[FirewallRule]:
        """Get all current rules"""
        return self.rules
    
    def load_rules(self) -> None:
        """Load rules from JSON file"""
        if os.path.exists(self.rules_file):
            try:
                with open(self.rules_file, 'r') as f:
                    rules_data = json.load(f)
                    self.rules = [FirewallRule(**rule) for rule in rules_data]
            except Exception as e:
                print(f"Error loading rules: {e}")
    
    def save_rules(self) -> None:
        """Save rules to JSON file"""
        try:
            rules_data = [vars(rule) for rule in self.rules]
            with open(self.rules_file, 'w') as f:
                json.dump(rules_data, f, indent=2)
        except Exception as e:
            print(f"Error saving rules: {e}")