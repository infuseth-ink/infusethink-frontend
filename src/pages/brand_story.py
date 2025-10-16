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


@ft.component
def AgentCard(
    name: str,
    tagline: str,
    description: str,
    image_path: str,
    coming_soon: bool = False,
):
    """Create an AI agent card with image, name, tagline and description."""
    # Brand colors
    MATCHA_GREEN = "#47905f"
    GOLDEN_OCHRE = "#e1c154"
    PARCHMENT_BEIGE = "#f6f0dd"

    return ft.Card(
        content=ft.Stack(
            controls=[
                # Main card content
                ft.Container(
                    content=ft.Column(
                        controls=[
                            # Agent Image
                            ft.Container(
                                content=ft.Image(
                                    src=image_path,
                                    width=240,
                                    height=240,
                                    border_radius=ft.BorderRadius.all(80),
                                ),
                                alignment=ft.Alignment(0.0, 0.0),
                                padding=ft.Padding.only(top=20, bottom=10),
                            ),
                            # Agent Name
                            ft.Text(
                                name,
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color=MATCHA_GREEN,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            # Tagline
                            ft.Text(
                                tagline,
                                size=14,
                                color=GOLDEN_OCHRE,
                                text_align=ft.TextAlign.CENTER,
                                italic=True,
                                weight=ft.FontWeight.W_500,
                            ),
                            # Description - with expand to fill remaining space
                            ft.Container(
                                content=ft.Text(
                                    description,
                                    size=13,
                                    text_align=ft.TextAlign.LEFT,
                                    color=ft.Colors.BLACK87,
                                ),
                                padding=ft.Padding.symmetric(horizontal=10),
                                expand=True,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=8,
                    ),
                    padding=ft.Padding.all(15),
                    bgcolor=PARCHMENT_BEIGE,
                    border_radius=ft.BorderRadius.all(12),
                    height=480,  # Fixed height for uniform card sizes
                ),
                # Coming Soon Badge (positioned in card, not on image)
                *(
                    [
                        ft.Container(
                            content=ft.Text(
                                "COMING SOON",
                                size=10,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            bgcolor=GOLDEN_OCHRE,
                            padding=ft.Padding.symmetric(horizontal=8, vertical=4),
                            border_radius=ft.BorderRadius.all(12),
                            top=10,
                            right=10,
                        )
                    ]
                    if coming_soon
                    else []
                ),
            ]
        ),
        elevation=2,
    )


@ft.component
def AIAgentsSection():
    """Create the responsive AI agents section with 3x2 layout for wide screens."""

    # Brand colors
    MATCHA_GREEN = "#47905f"
    GOLDEN_OCHRE = "#e1c154"

    # Agent data
    agents = [
        {
            "name": "TEAching Tagteam",
            "tagline": "AI-assisted tutorials and mentoring, 24/7",
            "description": "Steps in when the teacher can't be everywhere at once. With a teacher's loaded schedule and poor student-teacher ratios, TEAching Tagteam makes sure no learner is left behind.",
            "image": "agents/teacher-tagteam.png",
            "coming_soon": False,
        },
        {
            "name": "Mastery MATCHAr",
            "tagline": "Spaced practice and repeated attempts",
            "description": "Supports spaced practice and repeated attempts. MATCHAr helps learners revisit skills until mastery is achieved, proving that progress comes at different speeds for different students. It can brew learning paths appropriate to the learner's goal, styles, strengths, and weaknesses.",
            "image": "agents/mastery-matchar.png",
            "coming_soon": True,
        },
        {
            "name": "PU'ERpoint Partner",
            "tagline": "Presentation partner for structured delivery",
            "description": "The presentation partner for structured delivery. PU'ERpoint Pal organizes lessons, bootcamp slides, or training decks into clear, digestible flows that keep learners engaged. Currently only Sli.dev and PowerPoint are supported.",
            "image": "agents/puerpoint-partner.png",
            "coming_soon": True,
        },
        {
            "name": "CHA-llenger Crafter",
            "tagline": "Creates quizzes, homework, and assessments",
            "description": "Designs challenges that stretch learners without overwhelming them. CHAllenger Crafter ensures tasks are meaningful, motivating, and aligned with growth. Your goto AI-agent for creating quizzes, homework, and other assessments.",
            "image": "agents/challenge-crafter.png",
            "coming_soon": True,
        },
        {
            "name": "Marking MATÉ",
            "tagline": "First-pass evaluation with supportive feedback",
            "description": "First-pass evaluation, to be overridden by the instructor if needed. This agent provides feedback that's rigorous, strict, but supportive, giving learners clarity on where they stand and how to improve.",
            "image": "agents/marker-mate.png",
            "coming_soon": True,
        },
        {
            "name": "CHAIrman Collab",
            "tagline": "Manages non-teaching side of learning",
            "description": "Manages the non-teaching side of learning. From accreditation paperwork to certifications, bootcamps, and training compliance, CHAIrman Consultant ensures decisions are evidence-based and any paperworks are swiftly handled.",
            "image": "agents/chairman-collab.png",
            "coming_soon": True,
        },
    ]

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    "Six AI Agents",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=MATCHA_GREEN,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "To help educators and trainers with different aspects of teaching and learning.",
                    size=16,
                    text_align=ft.TextAlign.CENTER,
                    color=GOLDEN_OCHRE,
                ),
                ft.Container(height=20),  # Spacing
                # Responsive grid layout
                ft.ResponsiveRow(
                    controls=[
                        ft.Container(
                            content=AgentCard(
                                name=agent["name"],
                                tagline=agent["tagline"],
                                description=agent["description"],
                                image_path=agent["image"],
                                coming_soon=agent["coming_soon"],
                            ),
                            col={
                                "sm": 12,
                                "md": 6,
                                "lg": 4,
                            },  # Responsive: 1 col on small, 2 on medium, 3 on large
                            padding=ft.Padding.all(10),
                        )
                        for agent in agents
                    ],
                    spacing=0,
                ),
            ],
            spacing=15,
        ),
        padding=ft.Padding.all(20),
        margin=ft.Margin.only(bottom=30),
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
                # AI Agents Section
                AIAgentsSection(),
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
                                italic=True,
                            ),
                            ft.Text(
                                "Like tea leaves steeping in water, each learner's experiences, questions, "
                                "and insights infuse the learning space with unique flavor.",
                                size=16,
                            ),
                            ft.Text(
                                "The quill in our logo represents the act of capturing and shaping those infused ideas into "
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
                                    ft.Text(
                                        " is the invitation: bring your perspectives, your curiosity, your voice.",
                                        size=16,
                                    ),
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
                                    ft.Text(
                                        " is the promise: together, we'll transform those thoughts into outcomes that matter — personal mastery, community impact, and lifelong adaptability.",
                                        size=16,
                                    ),
                                ],
                                wrap=True,
                            ),
                        ],
                        spacing=15,
                    ),
                    padding=ft.Padding.all(20),
                    margin=ft.Margin.only(bottom=20),
                ),
                # Color Philosophy Section
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "Color Philosophy",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color=MATCHA_GREEN,
                            ),
                            ft.Column(
                                controls=[
                                    create_list_item(
                                        "Primary — Uji Matcha Green (#47905f): infusion, growth, focus.",
                                        size=14,
                                        color=MATCHA_GREEN,
                                    ),
                                    create_list_item(
                                        'Secondary — Golden Ochre (#e1c154): achievement, mastery, "wisdom more precious than gold" (Proverbs 16:16).',
                                        size=14,
                                        color=GOLDEN_OCHRE,
                                    ),
                                    create_list_item(
                                        "Tertiary — Warm Parchment Beige (#f6f0dd): tradition, the page, learner's space.",
                                        size=14,
                                    ),
                                ],
                                spacing=8,
                            ),
                        ],
                        spacing=15,
                    ),
                    padding=ft.Padding.all(20),
                    margin=ft.Margin.only(bottom=20),
                ),
                # Logo Narrative Section
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "Logo Narrative",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color=MATCHA_GREEN,
                            ),
                            ft.Text(
                                "The Infuseth.ink logo is built for clarity and meaning:",
                                size=16,
                                weight=ft.FontWeight.W_500,
                            ),
                            ft.Column(
                                controls=[
                                    create_list_item(
                                        "Bullseye precision — The circular teacup body doubles as a target, symbolizing hitting OBE learning outcomes.",
                                        size=14,
                                    ),
                                    create_list_item(
                                        "Quill strike — The nib lands at the center, representing accuracy, mastery, and the act of recording achievement.",
                                        size=14,
                                    ),
                                    create_list_item(
                                        "Magnifier lens — The same teacup circle can be read as a magnifying glass, highlighting focus, inquiry, and examination.",
                                        size=14,
                                    ),
                                    create_list_item(
                                        "Infusion swirl — The green interior shows the process of ideas steeping and evolving.",
                                        size=14,
                                    ),
                                    create_list_item(
                                        "Ink mark — The quill's path leads to a lasting imprint, the learner's future written in their own hand.",
                                        size=14,
                                    ),
                                ],
                                spacing=8,
                            ),
                            ft.Text(
                                "Every element is functional: no decorative extras, no unnecessary flourishes — just a direct visual story that aligns with the brand's mission.",
                                size=16,
                                italic=True,
                            ),
                        ],
                        spacing=15,
                    ),
                    padding=ft.Padding.all(20),
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
