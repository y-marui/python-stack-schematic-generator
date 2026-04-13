import matplotlib.axes
import matplotlib.figure
import matplotlib.pyplot as plt

from stack_schematic_generator.layer import Layer
from stack_schematic_generator.stack import Stack


class TestLayer:
    def test_defaults(self) -> None:
        layer = Layer("Si Sub.", "lightgray")
        assert layer.label == "Si Sub."
        assert layer.color == "lightgray"
        assert layer.width == 1
        assert layer.height == 1
        assert layer.slope == 0

    def test_custom_params(self) -> None:
        layer = Layer("W", "dodgerblue", width=2, height=0.5, slope=1)
        assert layer.width == 2
        assert layer.height == 0.5
        assert layer.slope == 1


class TestStack:
    def test_get_height_uniform(self) -> None:
        stack = Stack([Layer("A", "red"), Layer("B", "blue"), Layer("C", "green")])
        assert stack.get_height() == 3.0

    def test_get_height_with_positive_slope(self) -> None:
        # Layer A: height=1, slope=0 → contributes 1
        # Layer B: height=0.5, slope=1 → contributes 1.5
        stack = Stack(
            [
                Layer("A", "red"),
                Layer("B", "blue", height=0.5, slope=1),
            ]
        )
        assert stack.get_height() == 2.5

    def test_get_height_with_negative_slope(self) -> None:
        # Negative slope: max(slope, 0) = 0, so only height counts
        stack = Stack([Layer("A", "red", height=2, slope=-1)])
        assert stack.get_height() == 2.0

    def test_plot_returns_fig_ax(self) -> None:
        stack = Stack([Layer("Si Sub.", "lightgray"), Layer("W (3)", "dodgerblue")])
        fig, ax = stack.plot()
        assert isinstance(fig, matplotlib.figure.Figure)
        assert isinstance(ax, matplotlib.axes.Axes)
        plt.close(fig)

    def test_plot_axis_limits_extend_beyond_data(self) -> None:
        stack = Stack([Layer("A", "red")])
        fig, ax = stack.plot()
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        # Axes are padded slightly beyond the data range
        assert xlim[0] < 0
        assert xlim[1] > 1
        assert ylim[0] < 0
        assert ylim[1] > 0
        plt.close(fig)

    def test_plot_accepts_existing_fig_ax(self) -> None:
        stack = Stack([Layer("A", "red")])
        fig_in, ax_in = plt.subplots()
        fig_out, ax_out = stack.plot(fig=fig_in, ax=ax_in)
        assert fig_out is fig_in
        assert ax_out is ax_in
        plt.close(fig_in)
