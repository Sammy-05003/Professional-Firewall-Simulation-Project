import cmd
import ipaddress

class FirewallCLI(cmd.Cmd):
    intro = 'Welcome to the Firewall Simulator. Type help or ? to list commands.\n'
    prompt = '(firewall) '
    
    def __init__(self, firewall):
        super().__init__()
        self.firewall = firewall
    
    def do_add_rule(self, arg):
        """Add a new firewall rule: add_rule <ip_address> <port> <protocol> <action>
        Example: add_rule 192.168.1.1 80 TCP BLOCK"""
        try:
            ip_address, port, protocol, action = arg.split()
            
            # Validate IP address (allow * for wildcard)
            if ip_address != "*":
                ipaddress.ip_address(ip_address)
            
            # Validate port (allow * for wildcard)
            if port != "*":
                port_num = int(port)
                if not (0 <= port_num <= 65535):
                    raise ValueError("Port must be between 0 and 65535")
            
            # Validate protocol
            valid_protocols = ["TCP", "UDP", "ICMP", "*"]
            if protocol.upper() not in valid_protocols:
                raise ValueError(f"Protocol must be one of {valid_protocols}")
            
            # Validate action
            if action.upper() not in ["ALLOW", "BLOCK"]:
                raise ValueError("Action must be either ALLOW or BLOCK")
            
            self.firewall.rules_manager.add_rule(ip_address, port, protocol.upper(), action.upper())
            print("Rule added successfully")
            
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error adding rule: {e}")
    
    def do_list_rules(self, arg):
        """List all firewall rules"""
        rules = self.firewall.rules_manager.get_rules()
        if not rules:
            print("No rules defined")
            return
        
        print("\nCurrent Firewall Rules:")
        print("-" * 60)
        print(f"{'Index':<6} {'IP Address':<15} {'Port':<6} {'Protocol':<8} {'Action':<6}")
        print("-" * 60)
        
        for i, rule in enumerate(rules):
            print(f"{i:<6} {rule.ip_address:<15} {rule.port:<6} {rule.protocol:<8} {rule.action:<6}")
    
    def do_remove_rule(self, arg):
        """Remove a rule by index: remove_rule <index>"""
        try:
            index = int(arg)
            if self.firewall.rules_manager.remove_rule(index):
                print(f"Rule {index} removed successfully")
            else:
                print("Invalid rule index")
        except ValueError:
            print("Please provide a valid rule index")
    
    def do_test_packet(self, arg):
        """Test if a packet would be allowed: test_packet <ip_address> <port> <protocol>"""
        try:
            ip_address, port, protocol = arg.split()
            packet = Packet(ip_address, port, protocol.upper())
            allowed = self.firewall.process_packet(packet)
            status = "ALLOWED" if allowed else "BLOCKED"
            print(f"Packet would be {status}")
        except ValueError:
            print("Error: Please provide IP address, port, and protocol")
    
    def do_quit(self, arg):
        """Exit the firewall simulator"""
        print("Goodbye!")
        return True
    
    def start(self):
        self.cmdloop()