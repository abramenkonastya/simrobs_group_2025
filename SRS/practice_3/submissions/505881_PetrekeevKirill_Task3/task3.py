import mujoco
import mujoco.viewer
import time
import os

# os.environ['MUJOCO_GL'] = 'osmesa'
# model = mujoco.MjModel.from_xml_path("model.xml")
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "model.xml")

model = mujoco.MjModel.from_xml_path(model_path)
data = mujoco.MjData(model)

with mujoco.viewer.launch(model, data) as viewer:
    while viewer.is_running():
        mujoco.mj_step(model, data)
        viewer.sync()
        time.sleep(0.01)