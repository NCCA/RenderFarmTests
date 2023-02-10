import argparse


def ProcessCommandLine():
    parser = argparse.ArgumentParser(description="VRay Farm Submission Script")

    parser.add_argument(
        "--start_frame", "-s",  default=0, type=int, help="start frame for render sequence default 0",required=True,
    )
    parser.add_argument(
        "--name", "-n",  default="MyProject", type=str, help="Name of project ",
    )
    parser.add_argument(
        "--end_frame", "-e",  default=1, type=int, help="end frame for render sequence default 1",required=True,
    )

    parser.add_argument(
        "--by_frame", "-b", default=1, type=int, help="frame step for render default 1"
    )

    parser.add_argument(
        "--cpus", "-c",  default=2, type=int, help="number of cpus"
    )

    parser.add_argument("--scene_file", "-sc", help="scene file to render", required=True)
    parser.add_argument("--project_root", "-p", help="base of the project", required=True)
    w
    parser.add_argument("--remap", "-", help="Path to remap in destination, will try to do this automagically by default")

    parser.add_argument("--env","-en",action='append',nargs=2,metavar=('key','value'),help="Add extra environment variables in the form of KEY VALUE this will be sent to qube verbatim, you can specify multiples ")

    parser.add_argument("--debug","-d",action='store_true',help="enable debug mode, this will print out the package but not submit")

    parser.add_argument("--image_dir","-i",default="../images",type=str,help="alternative image directory")





    args = parser.parse_args()
    return args