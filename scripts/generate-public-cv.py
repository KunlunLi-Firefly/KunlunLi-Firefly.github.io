from pathlib import Path

from PIL import Image as PILImage
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
	HRFlowable,
	Image,
	KeepTogether,
	Paragraph,
	SimpleDocTemplate,
	Spacer,
	Table,
	TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "public" / "cv" / "kunlun-li-cv.pdf"
PHOTO = ROOT / "src" / "assets" / "images" / "profile" / "kunlun-li-cv.jpg"
TMP_PHOTO = ROOT / "tmp" / "pdfs" / "kunlun-li-cv-crop.jpg"

INK = colors.HexColor("#18222D")
MUTED = colors.HexColor("#596675")
ACCENT = colors.HexColor("#35B8C7")
SOFT = colors.HexColor("#EAF7F8")
WHITE = colors.white


def crop_photo() -> Path:
	"""Crop the portrait to a compact CV aspect ratio without cutting the head."""
	with PILImage.open(PHOTO) as source:
		image = source.convert("RGB")
		target_ratio = 0.78
		width, height = image.size
		current_ratio = width / height
		if current_ratio < target_ratio:
			new_height = int(width / target_ratio)
			top = max(0, int((height - new_height) * 0.30))
			image = image.crop((0, top, width, top + new_height))
		else:
			new_width = int(height * target_ratio)
			left = (width - new_width) // 2
			image = image.crop((left, 0, left + new_width, height))
		image.save(TMP_PHOTO, quality=92, optimize=True)
	return TMP_PHOTO


styles = getSampleStyleSheet()
name_style = ParagraphStyle(
	"Name",
	parent=styles["Normal"],
	fontName="Helvetica-Bold",
	fontSize=25,
	leading=28,
	textColor=INK,
	spaceAfter=4,
)
role_style = ParagraphStyle(
	"Role",
	parent=styles["Normal"],
	fontName="Helvetica-Bold",
	fontSize=10.2,
	leading=13,
	textColor=ACCENT,
	spaceAfter=7,
)
contact_style = ParagraphStyle(
	"Contact",
	parent=styles["Normal"],
	fontName="Helvetica",
	fontSize=8.5,
	leading=12,
	textColor=MUTED,
)
section_style = ParagraphStyle(
	"Section",
	parent=styles["Normal"],
	fontName="Helvetica-Bold",
	fontSize=10,
	leading=12,
	textColor=INK,
	spaceBefore=6,
	spaceAfter=4,
	uppercase=True,
)
entry_title_style = ParagraphStyle(
	"EntryTitle",
	parent=styles["Normal"],
	fontName="Helvetica-Bold",
	fontSize=9.2,
	leading=11.5,
	textColor=INK,
)
entry_meta_style = ParagraphStyle(
	"EntryMeta",
	parent=styles["Normal"],
	fontName="Helvetica",
	fontSize=8.1,
	leading=10.5,
	textColor=MUTED,
	alignment=TA_RIGHT,
)
body_style = ParagraphStyle(
	"Body",
	parent=styles["Normal"],
	fontName="Helvetica",
	fontSize=8.25,
	leading=10.8,
	textColor=INK,
	spaceAfter=2.5,
)
publication_style = ParagraphStyle(
	"Publication",
	parent=body_style,
	leftIndent=8,
	firstLineIndent=-8,
	spaceAfter=3,
)
footer_style = ParagraphStyle(
	"Footer",
	parent=styles["Normal"],
	fontName="Helvetica",
	fontSize=7.2,
	leading=9,
	textColor=MUTED,
	alignment=TA_RIGHT,
)


def section(title: str):
	return [
		Paragraph(title.upper(), section_style),
		HRFlowable(width="100%", thickness=0.7, color=ACCENT, spaceAfter=4),
	]


def entry(title: str, meta: str, detail: str | None = None):
	rows = [[Paragraph(title, entry_title_style), Paragraph(meta, entry_meta_style)]]
	table = Table(rows, colWidths=[126 * mm, 51 * mm], hAlign="LEFT")
	table.setStyle(
		TableStyle(
			[
				("VALIGN", (0, 0), (-1, -1), "TOP"),
				("LEFTPADDING", (0, 0), (-1, -1), 0),
				("RIGHTPADDING", (0, 0), (-1, -1), 0),
				("TOPPADDING", (0, 0), (-1, -1), 0),
				("BOTTOMPADDING", (0, 0), (-1, -1), 1),
			]
		)
	)
	items = [table]
	if detail:
		items.append(Paragraph(detail, body_style))
	return KeepTogether(items)


def build_cv() -> None:
	OUTPUT.parent.mkdir(parents=True, exist_ok=True)
	TMP_PHOTO.parent.mkdir(parents=True, exist_ok=True)
	photo_path = crop_photo()

	doc = SimpleDocTemplate(
		str(OUTPUT),
		pagesize=A4,
		rightMargin=16 * mm,
		leftMargin=16 * mm,
		topMargin=12 * mm,
		bottomMargin=11 * mm,
		title="Kunlun Li - Public CV",
		author="Kunlun Li",
		subject="Public professional curriculum vitae",
	)

	header_text = [
		Paragraph("KUNLUN LI", name_style),
		Paragraph(
			"APPLICATION ALGORITHM ENGINEER | MEDICAL IMAGING &amp; MACHINE LEARNING",
			role_style,
		),
		Paragraph(
			'Beijing, China&nbsp;&nbsp; | &nbsp;&nbsp;<a href="mailto:lkl2654462334@outlook.com" color="#35B8C7">lkl2654462334@outlook.com</a><br/>'
			'<a href="https://github.com/KunlunLi-Firefly" color="#35B8C7">github.com/KunlunLi-Firefly</a>&nbsp;&nbsp; | &nbsp;&nbsp;'
			'<a href="https://kunlunli-firefly.github.io" color="#35B8C7">kunlunli-firefly.github.io</a>',
			contact_style,
		),
	]
	photo = Image(str(photo_path), width=27 * mm, height=34.6 * mm)
	header = Table([[header_text, photo]], colWidths=[146 * mm, 31 * mm])
	header.setStyle(
		TableStyle(
			[
				("VALIGN", (0, 0), (-1, -1), "TOP"),
				("LEFTPADDING", (0, 0), (-1, -1), 0),
				("RIGHTPADDING", (0, 0), (0, 0), 6),
				("RIGHTPADDING", (1, 0), (1, 0), 0),
				("TOPPADDING", (0, 0), (-1, -1), 0),
				("BOTTOMPADDING", (0, 0), (-1, -1), 0),
			]
		)
	)

	story = [
		header,
		Spacer(1, 3),
		HRFlowable(width="100%", thickness=2.2, color=ACCENT, spaceAfter=2),
	]

	story.extend(section("Professional Experience"))
	story.append(
		entry(
			"Application Algorithm Engineer | blueballon",
			"Mar 2025 - Present | Beijing, China",
		)
	)

	story.extend(section("Research Experience"))
	story.append(
		entry(
			"Graduate Research Assistant | Johns Hopkins University",
			"May 2024 - Jan 2025 | Baltimore, MD",
			"Worked with Prof. Eric Nalisnick on depth-enhanced sign language recognition using monocular depth estimation, semi-supervised learning, and active learning under limited annotation.",
		)
	)
	story.append(
		entry(
			"Summer Research Program | UCLA",
			"Jun 2021 - Sep 2021 | Los Angeles, CA",
			"Studied gate-sizing optimization for digital integrated circuits, balancing delay and energy consumption under the supervision of Prof. Dejan Markovic.",
		)
	)

	story.extend(section("Education"))
	story.append(
		entry(
			"M.S., Electrical and Computer Engineering | Johns Hopkins University",
			"Aug 2023 - Jan 2025",
		)
	)
	story.append(
		entry(
			"B.E., Electrical Engineering | University of Mississippi",
			"Aug 2021 - May 2023",
		)
	)
	story.append(
		entry(
			"B.E., Electrical Information Engineering | North China University of Technology",
			"Sep 2019 - Jun 2021",
		)
	)

	story.extend(section("Selected Research Projects"))
	story.append(
		entry(
			"Deep Learning-Based Liver and Tumor Segmentation",
			"2024",
			"Compared U-Net, Attention U-Net, and DALU-Net on 3D-IRCADb CT data. The project report records a DALU-Net Dice coefficient of 0.899, compared with 0.822 for the U-Net baseline.",
		)
	)
	story.append(
		entry(
			"Evaluation of Subarachnoid-Space Volume in MRI",
			"2024",
			"Built a coursework pipeline using FSL, FastSurfer, CycleGAN, K-means clustering, and morphology for MRI registration, synthesis, segmentation, and quantitative analysis.",
		)
	)
	story.append(
		entry(
			"Epoch Extraction for Speaker Differentiation",
			"2023 - 2024",
			"Implemented zero-frequency filtering and a locking-based comparison workflow for CMU ARCTIC speech data, with an implementation path toward Raspberry Pi and hardware-oriented systems.",
		)
	)

	story.extend(section("Selected Publications and Manuscripts"))
	publications = [
		'<b>K. Li</b>, D. Ferro, X. Zhao, A. J. Syed, A. K. Vuppala, and A. Syed. "Matlab-based Epoch Extraction for Speaker Differentiation." <i>arXiv:2407.18447</i>, 2024. <a href="https://arxiv.org/abs/2407.18447" color="#35B8C7">arXiv</a>',
		'<b>K. Li</b>, J. Ma, and Y. Zhang. "Optimization of a Three-Bit Absolute Value Detector with Domino Logic and Gate Sizing." <i>Proceedings of SPIE 12161</i>, 2022. <a href="https://doi.org/10.1117/12.2627237" color="#35B8C7">doi:10.1117/12.2627237</a>',
		'R. Chen, <b>K. Li</b>, Y. Wang, and E. Nalisnick. "SSLAL: Leveraging Semi-Supervised and Active Learning for Robust Depth-Enhanced Sign Language Recognition." Unpublished manuscript, 2024.',
	]
	for publication in publications:
		story.append(Paragraph(f"- {publication}", publication_style))

	story.extend(section("Technical Skills"))
	story.append(
		Paragraph(
			"<b>Programming:</b> Python, MATLAB&nbsp;&nbsp; | &nbsp;&nbsp;<b>Frameworks and tools:</b> PyTorch, FSL, FastSurfer, MIPAV, LaTeX&nbsp;&nbsp; | &nbsp;&nbsp;<b>Languages:</b> Mandarin (native), English (fluent), Japanese (beginner)",
			body_style,
		)
	)
	story.append(Spacer(1, 3))
	story.append(
		Table(
			[[Paragraph("Public CV - Updated August 2026", footer_style)]],
			colWidths=[177 * mm],
			style=TableStyle(
				[
					("BACKGROUND", (0, 0), (-1, -1), SOFT),
					("LEFTPADDING", (0, 0), (-1, -1), 5),
					("RIGHTPADDING", (0, 0), (-1, -1), 5),
					("TOPPADDING", (0, 0), (-1, -1), 3),
					("BOTTOMPADDING", (0, 0), (-1, -1), 3),
				]
			),
		)
	)

	doc.build(story)
	print(OUTPUT)


if __name__ == "__main__":
	build_cv()
