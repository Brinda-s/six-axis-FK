import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

kivy.require('2.0.0')

class RobotController(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.joint_values = [0, 0, 0, 0, 0, 0, 0]

    def increase_value(self, joint_index):
        self.joint_values[joint_index] += 1
        self.update_label(joint_index)

    def decrease_value(self, joint_index):
        if self.joint_values[joint_index] > 0:
            self.joint_values[joint_index] -= 1
        self.update_label(joint_index)

    def update_label(self, joint_index):
        label = self.root.ids[f"joint_{joint_index}_label"]
        label.text = str(self.joint_values[joint_index])

    def build(self):
        root = BoxLayout(orientation='vertical', spacing=10)
        
        for i in range(7):
            joint_layout = BoxLayout(orientation='horizontal', spacing=10)
            
            joint_label = Label(text=f"Joint {i+1}:")
            joint_layout.add_widget(joint_label)
            
            minus_button = Button(text="-")
            minus_button.bind(on_release=lambda btn, index=i: self.decrease_value(index))
            joint_layout.add_widget(minus_button)
            
            joint_value_label = Label(text="0")
            joint_layout.add_widget(joint_value_label)
            root.ids[f"joint_{i}_label"] = joint_value_label
            
            plus_button = Button(text="+")
            plus_button.bind(on_release=lambda btn, index=i: self.increase_value(index))
            joint_layout.add_widget(plus_button)
            
            root.add_widget(joint_layout)

        return root

if __name__ == '__main__':
    RobotController().run()


