import json

class DesignNode:
    """Represents a single step in the Program Design Journey."""
    def __init__(self, step_id, step_name, prompt):
        self.step_id = step_id
        self.step_name = step_name
        self.prompt = prompt
        self.user_input = None
        self.next = None  # Linked List pointer

class LeaderPathWizard:
    def __init__(self):
        # 1. Linked List Setup: The Design Journey
        self.head = DesignNode(1, "Problem Definition", "What is the core educational challenge?")
        step2 = DesignNode(2, "Stakeholder Mapping", "Who are the primary stakeholders (e.g., Teachers, HMs)?")
        step3 = DesignNode(3, "Outcome Setting", "What is the specific goal for these stakeholders?")
        step4 = DesignNode(4, "Impact Indicator", "How will you measure success (e.g., test scores)?")
        
        # Connecting the nodes (The "Guided Path")
        self.head.next = step2
        step2.next = step3
        step3.next = step4
        
        self.current = self.head
        self.history = []  # Stack for 'Undo' functionality
        
        # 2. Pattern Library: Dictionary for O(1) Templates
        self.templates = {
            "FLN": "Foundational Literacy & Numeracy: Focused on early grade reading/math.",
            "Coaching": "Teacher Mentoring: Focused on regular classroom observation/feedback.",
            "Digital": "Smart Classroom: Focused on integrating EdTech in rural DIETs."
        }

    def get_template_suggestion(self, category):
        """Efficiency feature: Instant lookup for proven logic."""
        return self.templates.get(category, "Custom Template Selected.")

    def process_input(self, data):
        """Moves the wizard forward and saves state to history stack."""
        if self.current:
            self.history.append((self.current, self.current.user_input)) # Push to Stack
            self.current.user_input = data
            self.current = self.current.next
            return True
        return False

    def undo(self):
        """Pops the last state from the stack to go back."""
        if self.history:
            self.current, prev_input = self.history.pop()
            print(f"--- Reverting to: {self.current.step_name} ---")
            return True
        return False

    def export_lfa(self):
        """Traverses the Linked List to generate the final design."""
        print("\n" + "="*40)
        print(" FINAL LOGICAL FRAMEWORK (LFA) ")
        print("="*40)
        temp = self.head
        while temp:
            status = temp.user_input if temp.user_input else "NOT COMPLETED"
            print(f"Step {temp.step_id} - {temp.step_name}: {status}")
            temp = temp.next
        print("="*40)

# --- WORKFLOW DEMO ---
def start_wizard():
    wizard = LeaderPathWizard()
    print("Welcome to LeaderPath: ShikshaLokam Program Design Assistant\n")
    
    # Example: User selects a template
    print(f"Suggested Model: {wizard.get_template_suggestion('FLN')}\n")
    
    # Walking through the Nodes
    while wizard.current:
        print(f"Current Step: {wizard.current.step_name}")
        val = input(f"PROMPT: {wizard.current.prompt}\n>> ")
        
        if val.lower() == 'back':
            wizard.undo()
        else:
            wizard.process_input(val)
            print("-" * 20)
            
    # Final Output
    wizard.export_lfa()

if __name__ == "__main__":
    # In a real app, this would be a web interface.
    # For the Prototype Phase, this CLI proves the logic.
    start_wizard()
