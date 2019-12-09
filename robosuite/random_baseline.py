import numpy as np
import robosuite as suite

if __name__ == "__main__":
    envs = sorted(suite.environments.ALL_ENVS)

    env = suite.make(
        "SawyerPickPlace",
        has_renderer=True,
        ignore_done=True,
        use_camera_obs=False,
        control_freq=100,
    )

    env.reset()
    env.viewer.set_camera(camera_id=0)

    for i in range(10000):
        env.render()

    print(env.obj_to_use)
