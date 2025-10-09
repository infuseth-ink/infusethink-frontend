"""Brand Story page for Infuseth.ink"""

import flet as ft


def create_list_item(text, size=14, color=None) -> ft.Row:
    """Create a proper list item with bullet point."""
    return ft.Row(
        controls=[
            ft.Icon(
                ft.Icons.FIBER_MANUAL_RECORD, size=6, color=color or ft.Colors.BLACK54
            ),
            ft.Text(text, size=size, expand=True),
        ],
        spacing=10,
        tight=True,
    )


def create_brand_story_page() -> ft.Container:
    """Create the brand story page with rich content based on the brand narrative."""

    # Brand colors from the story
    MATCHA_GREEN = "#47905f"
    GOLDEN_OCHRE = "#e1c154"
    PARCHMENT_BEIGE = "#f6f0dd"

    return ft.Container(
        content=ft.Column(
            controls=[
                # Hero Section
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "Infuseth.ink",
                                size=48,
                                weight=ft.FontWeight.BOLD,
                                color=MATCHA_GREEN,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Text(
                                "Infuse thoughts. Ink futures.",
                                size=24,
                                style=ft.TextThemeStyle.HEADLINE_SMALL,  # type: ignore[arg-type]
                                color=GOLDEN_OCHRE,
                                text_align=ft.TextAlign.CENTER,
                                italic=True,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10,
                    ),
                    padding=ft.Padding.all(40),
                    bgcolor=PARCHMENT_BEIGE,
                    border_radius=ft.BorderRadius.all(12),
                    margin=ft.Margin.only(bottom=30),
                ),
                # Pronunciation Section
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "Pronunciation",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color=MATCHA_GREEN,
                            ),
                            ft.Text("It's up to you! 😄", size=16),
                            ft.Column(
                                controls=[
                                    create_list_item(
                                        "in-FYOOS-eth ink — Shakespearean / King James bible flare",
                                        size=14,
                                    ),
                                    ft.Container(
                                        content=ft.Text(
                                            'like "giveth" or "speaketh"',
                                            size=12,
                                            italic=True,
                                        ),
                                        padding=ft.Padding.only(left=20),
                                    ),
                                    create_list_item(
                                        "infuse think — the modern, conceptual reading",
                                        size=14,
                                    ),
                                    create_list_item(
                                        "infuseth dot ink — the tech-brand URL readout",
                                        size=14,
                                    ),
                                ],
                                spacing=8,
                            ),
                        ],
                        spacing=10,
                    ),
                    padding=ft.Padding.all(20),
                    margin=ft.Margin.only(bottom=20),
                ),
                # Brand Narrative Section
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "Brand Narrative",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color=MATCHA_GREEN,
                            ),
                            ft.Text(
                                "Infuseth.ink is built on the conviction that all students can learn — "
                                "a core principle championed by William Spady's Outcome-Based Education (OBE).",
                                size=16,
                            ),
                            ft.Text(
                                "We believe learning is not a one-size-fits-all event, but a living process: "
                                "not the same day, not the same way.",
                                size=16,
                                weight=ft.FontWeight.W_500,
                            ),
                            ft.Text(
                                "Like tea leaves steeping in water, each learner's experiences, questions, "
                                "and insights infuse the learning space with unique flavor. The quill in our "
                                "logo represents the act of capturing and shaping those infused ideas into "
                                'something lasting — the "ink" that marks futures.',
                                size=16,
                            ),
                            ft.Row(
                                controls=[
                                    ft.Container(
                                        content=ft.Text(
                                            "Infuse thoughts",
                                            size=18,
                                            weight=ft.FontWeight.BOLD,
                                            color=MATCHA_GREEN,
                                        ),
                                        padding=ft.Padding.all(10),
                                        bgcolor=ft.Colors.with_opacity(
                                            0.1, MATCHA_GREEN
                                        ),
                                        border_radius=ft.BorderRadius.all(8),
                                    ),
                                    ft.Text(" is the invitation", size=16),
                                ],
                                wrap=True,
                            ),
                            ft.Row(
                                controls=[
                                    ft.Container(
                                        content=ft.Text(
                                            "Ink futures",
                                            size=18,
                                            weight=ft.FontWeight.BOLD,
                                            color=GOLDEN_OCHRE,
                                        ),
                                        padding=ft.Padding.all(10),
                                        bgcolor=ft.Colors.with_opacity(
                                            0.1, GOLDEN_OCHRE
                                        ),
                                        border_radius=ft.BorderRadius.all(8),
                                    ),
                                    ft.Text(" is the promise", size=16),
                                ],
                                wrap=True,
                            ),
                        ],
                        spacing=15,
                    ),
                    padding=ft.Padding.all(20),
                    margin=ft.Margin.only(bottom=20),
                ),
                # Core Feature Section
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "Core Feature",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color=MATCHA_GREEN,
                            ),
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Text(
                                            "Level Matcha",
                                            size=24,
                                            weight=ft.FontWeight.BOLD,
                                            color=MATCHA_GREEN,
                                        ),
                                        ft.Text(
                                            '"level matcher"',
                                            size=16,
                                            italic=True,
                                            color=GOLDEN_OCHRE,
                                        ),
                                        ft.Text(
                                            "Matches lessons and materials to the learner's level and learning style.",
                                            size=16,
                                        ),
                                        ft.Column(
                                            controls=[
                                                create_list_item(
                                                    "Generative AI explainers and visual aids",
                                                    size=14,
                                                    color=MATCHA_GREEN,
                                                ),
                                                create_list_item(
                                                    "Adaptive learning paths",
                                                    size=14,
                                                    color=MATCHA_GREEN,
                                                ),
                                                create_list_item(
                                                    "Learning activities tailored to individual needs",
                                                    size=14,
                                                    color=MATCHA_GREEN,
                                                ),
                                            ],
                                            spacing=8,
                                        ),
                                    ],
                                    spacing=10,
                                ),
                                padding=ft.Padding.all(20),
                                bgcolor=ft.Colors.with_opacity(0.05, MATCHA_GREEN),
                                border_radius=ft.BorderRadius.all(12),
                                border=ft.Border.all(2, MATCHA_GREEN),
                            ),
                        ],
                        spacing=15,
                    ),
                    padding=ft.Padding.all(20),
                    margin=ft.Margin.only(bottom=20),
                ),
                # ArCHAIve Feature Teaser
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "☕ Coming Soon: Accreditation ArCHAIve",
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color=GOLDEN_OCHRE,
                            ),
                            ft.Text(
                                "Accreditation assistant that steeps handwritten notes, scanned forms, "
                                "and activity logs into structured, reviewer-ready archives.",
                                size=14,
                            ),
                            ft.Text(
                                '"Steeping every paper into lasting accreditation objective evidence."',
                                size=14,
                                italic=True,
                                color=MATCHA_GREEN,
                            ),
                        ],
                        spacing=10,
                    ),
                    padding=ft.Padding.all(20),
                    bgcolor=ft.Colors.with_opacity(0.05, GOLDEN_OCHRE),
                    border_radius=ft.BorderRadius.all(12),
                    margin=ft.Margin.only(bottom=20),
                ),
                # Philosophy Footer
                ft.Container(
                    content=ft.Text(
                        "Infuseth.ink is more than a tool — it's a philosophy.\n"
                        "Every learner, every thought, every future is worth the infusion.",
                        size=16,
                        text_align=ft.TextAlign.CENTER,
                        style=ft.TextThemeStyle.BODY_MEDIUM,  # type: ignore[arg-type]
                        color=MATCHA_GREEN,
                        weight=ft.FontWeight.W_500,
                    ),
                    padding=ft.Padding.all(30),
                    bgcolor=PARCHMENT_BEIGE,
                    border_radius=ft.BorderRadius.all(12),
                    margin=ft.Margin.only(bottom=30),
                ),
            ],
            spacing=0,
            scroll=ft.ScrollMode.AUTO,
        ),
        padding=ft.Padding.all(20),
        expand=True,
    )
