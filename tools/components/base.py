from streamlit.delta_generator import DeltaGenerator
from abc import ABC, abstractmethod
from typing import Dict
import streamlit as st


class Canvas:
    # Components
    components: Dict[str, 'Component'] = {}
    
    def __init__(self):
        # Rendering Elements
        self.canvas         = st.container()
        self.instructions   = st.empty()
        self.status         = st.empty()
    
    @classmethod
    def from_components(
        cls,
        components: Dict[str, 'Component']
    ):
        instance = cls()
        for name, component in components.items():
            instance.components[name] = component
        return instance

    def render(self, component_name: str):
        return self.components[component_name](self).run()


class Component(ABC):
    def __init__(self, canvas: 'Canvas'):
        self.canvas = canvas
    
    @abstractmethod
    def run(self):
        pass
    
    def get_element(self, element_name: str) -> DeltaGenerator:
        try:
            element = getattr(self.canvas, element_name)
            assert isinstance(element, DeltaGenerator)
            return element
        except AttributeError:
            raise AttributeError(f"Element {element_name} does not exist on canvas.")



