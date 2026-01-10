class DesignNode:
    def __init__(self, step_id, step_name, prompt, description):
        self.step_id = step_id
        self.step_name = step_name
        self.prompt = prompt
        self.description = description # Added for a realistic UI
        self.user_input = ""
        self.next = None

class LeaderPathWizard:
    def __init__(self):
        # Realistic educational design steps
        self.head = DesignNode(1, "Problem Definition", "What is the core educational challenge?", "Clearly define the gap you are trying to bridge in the current system.")
        node2 = DesignNode(2, "Stakeholder Mapping", "Who are the primary stakeholders?", "Identify students, teachers, or parents who will be impacted.")
        node3 = DesignNode(3, "Impact Indicators", "How will you measure success?", "Define measurable goals like '20% increase in literacy'.")
        
        self.head.next = node2
        node2.next = node3
        self.current = self.head

    def process_input(self, data):
        if self.current:
            self.current.user_input = data
            self.current = self.current.next