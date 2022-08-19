from setuptools import setup


if __name__ == '__main__':
    setup(
        name="detr",
        version="0.2.0",
        packages=[
            "detr",
            "detr.d2",
            "detr.d2.detr",
            "detr.d2.configs",
            "detr.datasets",
            "detr.models",
            "detr.util",
        ],
    )
