from gradio.themes.base import Base
from gradio.themes.utils import colors, fonts, sizes


def create_color(name: str, value: str) -> colors.Color:
    return colors.Color(
        name=name,
        c50=value,
        c100=value,
        c200=value,
        c300=value,
        c400=value,
        c500=value,
        c600=value,
        c700=value,
        c800=value,
        c900=value,
        c950=value,
    )

ibm_blue = create_color("ibm_blue", "#0F62FE")


class IBMTheme(Base):
    def __init__(
        self,
        *,
        primary_hue: colors.Color | str = ibm_blue,
        secondary_hue: colors.Color | str = colors.emerald,
        neutral_hue: colors.Color | str = colors.gray,
        spacing_size: sizes.Size | str = sizes.spacing_md,
        radius_size: sizes.Size | str = sizes.radius_md,
        text_size: sizes.Size | str = sizes.text_lg,
        font: fonts.Font
        | str
        | list[fonts.Font | str] = (
            "IBM Plex Serif",
            fonts.GoogleFont("IBM Plex Serif"),
            "ui-sans-serif",
            "sans-serif",
        ),
        font_mono: fonts.Font
        | str
        | list[fonts.Font | str] = (
            "IBM Plex Mono",
            fonts.GoogleFont("IBM Plex Mono"),
            "ui-monospace",
            "monospace",
        ),
    ):
        super().__init__(
            primary_hue=primary_hue,
            secondary_hue=secondary_hue,
            neutral_hue=neutral_hue,
            spacing_size=spacing_size,
            radius_size=radius_size,
            text_size=text_size,
            font=font,
            font_mono=font_mono,
        )
