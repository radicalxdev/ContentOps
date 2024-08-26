BASE_PROMPT = """
You are a text to YAML converter. You are given structured text which is organized into a series of screens that have action buttons that connect to other screens. You are to convert this text into YAML format. 


Observe and follow the examples:

### Input
```text
### **Screen 1: Welcome to the Alfred AI Development Team**

**Ada:**

"Welcome aboard, {{username}}! It's great to have you on the Alfred AI development team. I’ve been assigned to help get you up to speed on one of our most critical projects: the **Project Management API**. This API is the backbone of Alfred AI's new project management tool. It's designed to streamline project and task management for teams across various industries by allowing them to efficiently manage project data, assign tasks, track progress, and meet deadlines."

**Learner:**

[Response]

**CTA:** Continue

---

### **Screen 2: Your Mission**

**Ada:**

"Now that you’re on board, let’s dive into your first mission. The **Project Management API** is vital for our enterprise clients who manage large-scale projects with multiple teams. To ensure the success of this tool, it needs to handle complex project data with high efficiency and reliability."

**Learner:**

[Response]

**CTA:** "Tell me more about the task."

---

### **Screen 3: Mission Objectives**

**Ada:**

"Your immediate task is to enhance the API by refining the CRUD operations—Create, Read, Update, Delete—for managing projects and tickets. These operations are the backbone of the API’s functionality, and they must be robust, scalable, and secure to meet our clients’ needs."

**Learner:**

[Response]

**CTA:** "What are the specific user stories?"

---

### **Screen 4: Scenario Details**

**Ada:**

"To give you some context, here are the key user stories we’re focusing on:

- **User Story 1: Project Creation**
    
    'As a project manager, I need to create new projects within the system, including setting a project name, description, and assigning it to a team, so that I can start organizing tasks and resources efficiently.'
    
- **User Story 2: Ticket Management**
    
    'As a project manager, I want to be able to create, view, update, and delete tickets within a project, so that I can keep track of tasks, deadlines, and team assignments.'"
    

**Learner:**

[Response]

**CTA:** "I’m ready to start!" → Continue

---

### **Screen 5: Challenges with CRUD Operations**

**Ada:**

"Before we jump into the implementation, let’s talk about some common challenges you might face when developing CRUD operations. From your experience, what aspects of building these operations do you find most time-consuming or frustrating?"

**Learner Response Options:**

1. "Honestly, getting the basic structure right without wasting time."
2. "Maintaining consistency and quality across the codebase."
3. "Handling error cases efficiently without cluttering the code."

**CTA:** Select an option to proceed.

---

### **Screen 6a: GitHub Copilot Benefits - Structure**

**Ada:**

"That’s a challenge many developers face. GitHub Copilot is designed to tackle exactly this issue. It can quickly suggest the foundational blocks of CRUD operations based on simple comments you write, saving you time and allowing you to focus on the more complex parts of the development."

**CTA:** "Show me Copilot in action."

---

### **Screen 6b: GitHub Copilot Benefits - Consistency**

**Ada:**

"Consistency is key, especially in large projects. Copilot helps by suggesting code that aligns with best practices, ensuring that your CRUD operations not only work but are also up to standard with the rest of your codebase."

**CTA:** "Let’s see how Copilot can help."

---

### **Screen 6c: GitHub Copilot Benefits - Error Handling**

**Ada:**

"Error handling can be tricky, and it's crucial to get it right. Copilot can assist by generating robust error-handling code, helping you manage edge cases effectively without adding unnecessary complexity to your code."

**CTA:** "I’m ready to try this out."

---

### **Screen 7: Cloning the Repository <github_setup>**

**Ada:**

"Before we dive into development setup, let’s make sure you have the project repository ready. Clone the repository we’ll be working on: [Alfred AI Project Management API](https://github.com/alfred-ai-co/w2-python-code-generation-and-completion). This is where your team’s work is already underway. We’ll be picking up where they left off."

**CTA:** "Repository cloned."

---

### **Screen 8: Development Setup**

**Ada:**

"Your team has already made significant contributions to the Project Management API on GitHub, and now it's your turn to dive in! Our goal is to contribute the CRUD operations and eventually create a pull request for review. Let’s start by making sure your development environment is ready."

**CTA:** "Let’s set up the environment."

---

### **Screen 9: Setting Up Your Environment**

**Ada:**

"We'll be using Visual Studio Code, which offers excellent support for Python development and seamless integration with GitHub Copilot. Make sure the Python extension is installed and active. To streamline your workflow, I recommend using a Python Virtual Environment for managing dependencies. This is also outlined in the project's [README.md](http://readme.md/) file."

**Learner:**

[Response]

**CTA:** "Environment is set up."

---

### **Screen 10: Final Setup Steps**

**Ada:**

"Within the repository, set up your environment according to the README.md file. Ensure that you’ve created a dev.env and prod.env file based on the env.example, setting the APP_ENV variable to either 'dev' or 'prod'. By default, we’ll work in the dev environment."

**Learner:**

[Response]

**CTA:** "Environment configured."

---

### **Screen 11: Activating Your Environment**

**Ada:**

"In the terminal, activate the shell script with the command: /start.sh <args>, where you can set dev or prod as the argument. By default, a dev environment is instantiated. This will get your environment up and running."

**Learner:**

[Action completed]

**CTA:** "Everything’s set up."

---

### **Screen 12: Confirming GitHub Copilot and Environment Setup**

**Ada:**

"Before we dive into the code, let's make sure everything is ready to go. Please confirm the following:

1. **GitHub Copilot Subscription**: Ensure your GitHub account is subscribed to GitHub Copilot. You can use the free trial if you haven't already.
2. **Extensions Installed**: Verify that the GitHub Copilot and Copilot Chat extensions are installed and active in Visual Studio Code.

Once you've confirmed these steps, we'll be all set to move forward!"

**Learner:**

[Everything’s set up]

**CTA:** "Let’s dive into the code."


### Output YAML
```yaml
nodes:
- id: screen1
  type: message
  body:
    parts:
    - type: text
      content: |
        Welcome aboard, {{username}}! It's great to have you on the Alfred AI development team. I’ve been assigned to help get you up to speed on one of our most critical projects: the **Project Management API**. This API is the backbone of Alfred AI's new project management tool. It's designed to streamline project and task management for teams across various industries by allowing them to efficiently manage project data, assign tasks, track progress, and meet deadlines.
  edges:
  - target_node_id: screen2
    text: Continue

- id: screen2
  type: message
  body:
    parts:
    - type: text
      content: |
        Now that you’re on board, let’s dive into your first mission. The **Project Management API** is vital for our enterprise clients who manage large-scale projects with multiple teams. To ensure the success of this tool, it needs to handle complex project data with high efficiency and reliability.
  edges:
  - target_node_id: screen3
    text: Tell me more about the task.

- id: screen3
  type: message
  body:
    parts:
    - type: text
      content: |
        Your immediate task is to enhance the API by refining the CRUD operations—Create, Read, Update, Delete—for managing projects and tickets. These operations are the backbone of the API’s functionality, and they must be robust, scalable, and secure to meet our clients’ needs.
  edges:
  - target_node_id: screen4
    text: What are the specific user stories?

- id: screen4
  type: message
  body:
    parts:
    - type: text
      content: |
        To give you some context, here are the key user stories we’re focusing on:

        - **User Story 1: Project Creation**

          'As a project manager, I need to create new projects within the system, including setting a project name, description, and assigning it to a team, so that I can start organizing tasks and resources efficiently.'

        - **User Story 2: Ticket Management**

          'As a project manager, I want to be able to create, view, update, and delete tickets within a project, so that I can keep track of tasks, deadlines, and team assignments.'
  edges:
  - target_node_id: screen5
    text: I’m ready to start!

- id: screen5
  type: message
  body:
    parts:
    - type: text
      content: |
        Before we jump into the implementation, let’s talk about some common challenges you might face when developing CRUD operations. From your experience, what aspects of building these operations do you find most time-consuming or frustrating?
  edges:
  - target_node_id: screen6a
    text: "Honestly, getting the basic structure right without wasting time."
  - target_node_id: screen6b
    text: "Maintaining consistency and quality across the codebase."
  - target_node_id: screen6c
    text: "Handling error cases efficiently without cluttering the code."

- id: screen6a
  type: message
  body:
    parts:
    - type: text
      content: |
        That’s a challenge many developers face. GitHub Copilot is designed to tackle exactly this issue. It can quickly suggest the foundational blocks of CRUD operations based on simple comments you write, saving you time and allowing you to focus on the more complex parts of the development.
  edges:
  - target_node_id: screen7
    text: Show me Copilot in action.

- id: screen6b
  type: message
  body:
    parts:
    - type: text
      content: |
        Consistency is key, especially in large projects. Copilot helps by suggesting code that aligns with best practices, ensuring that your CRUD operations not only work but are also up to standard with the rest of your codebase.
  edges:
  - target_node_id: screen7
    text: Let’s see how Copilot can help.

- id: screen6c
  type: message
  body:
    parts:
    - type: text
      content: |
        Error handling can be tricky, and it's crucial to get it right. Copilot can assist by generating robust error-handling code, helping you manage edge cases effectively without adding unnecessary complexity to your code.
  edges:
  - target_node_id: screen7
    text: I’m ready to try this out.

- id: screen7
  type: message
  body:
    parts:
    - type: text
      content: |
        Before we dive into development setup, let’s make sure you have the project repository ready. 
        Clone the repository we’ll be working on: [Alfred AI Project Management API](https://github.com/alfred-ai-co/w2-python-code-generation-and-completion). 
        This is where your team’s work is already underway. We’ll be picking up where they left off.
  edges:
  - target_node_id: screen8
    text: Repository cloned.

- id: screen8
  type: message
  body:
    parts:
    - type: text
      content: |
        Your team has already made significant contributions to the Project Management API on GitHub, and now it's your turn to dive in! Our goal is to contribute the CRUD operations and eventually create a pull request for review. Let’s start by making sure your development environment is ready.
  edges:
  - target_node_id: screen9
    text: Let’s set up the environment.

- id: screen9
  type: message
  body:
    parts:
    - type: text
      content: |
        We'll be using Visual Studio Code, which offers excellent support for Python development and seamless integration with GitHub Copilot. Make sure the Python extension is installed and active. To streamline your workflow, I recommend using a Python Virtual Environment for managing dependencies. This is also outlined in the project's [README.md](http://readme.md/) file.
  edges:
  - target_node_id: screen10
    text: Environment is set up.

- id: screen10
  type: message
  body:
    parts:
    - type: text
      content: |
        Within the repository, set up your environment according to the `README.md` file. Ensure that you’ve created a `dev.env` and `prod.env` file based on the `env.example`, setting the `APP_ENV` variable to either 'dev' or 'prod'. By default, we’ll work in the `dev` environment.
  edges:
  - target_node_id: screen11
    text: Environment configured.

- id: screen11
  type: message
  body:
    parts:
    - type: text
      content: |
        In the terminal, activate the shell script with the command: `/start.sh <args>`, where you can set `dev` or `prod` as the argument. By default, a `dev` environment is instantiated. This will get your environment up and running.
  edges:
  - target_node_id: screen12
    text: Everything’s set up.

- id: screen12
  type: message
  body:
    parts:
    - type: text
      content: |
        Before we dive into the code, let's make sure everything is ready to go. Please confirm the following:

        1. **GitHub Copilot Subscription**: Ensure your GitHub account is subscribed to GitHub Copilot. You can use the free trial if you haven't already.
        2. **Extensions Installed**: Verify that the GitHub Copilot and Copilot Chat extensions are installed and active in Visual Studio Code.

        Once you've confirmed these steps, we'll be all set to move forward!
  edges:
  - target_node_id: END
    text: Let’s dive into the code.

- id: END
  type: message
  body:
    parts:
    - type: text
      content: |
        This concludes the setup process. You are now ready to start contributing to the Project Management API. 

        Let's dive into the code and start enhancing the CRUD operations.
```

Human:
{text}
"""


CONTEXT_PROMPT = """
Given the following output yaml, create a single paragraph which describes what the content is about. Be as descriptive as you require. You're writing this paragraph for other LLMs or educators to utilize as context for whenever the learner is asking for help

Example output paragraph:
In this mission, learners are introduced to the 'Creating Code Using GitHub
    Copilot Inline Chat' task, where they will contribute to the development of an
    MVP for Alfred AI's Project Management API. The mission focuses on building ticket
    routes and their respective data operations, leveraging GitHub Copilot's inline
    chat feature for contextual coding interactions. Learners are guided to start
    the mission or learn more about the scenario, which involves using an existing
    project management API. This exercise demonstrates the practical application of
    GitHub Copilot's features to enhance development efficiency and interaction.

Example output paragraph 2:
This mission is focused on enhancing a Project Management API by incorporating ticket management functionalities. It begins with a welcoming message that acknowledges the learner's previous work on CRUD operations and introduces the new task of implementing ticket management, which is essential for tracking tasks and issues within projects. The dialogue progresses through three screens, guiding the learner to prepare their development environment by creating a new file named tickets.py in the specified directory. It then delves into the specifics of the project, presenting two critical user stories: one for creating tickets, which involves defining attributes like title and description, and another for tracking tickets, allowing project managers to view, update, and delete them. The learner is prompted to implement the necessary routes and data operations based on these user stories, fostering an interactive and practical learning experience in API development.

### YAML:
{yaml}
"""