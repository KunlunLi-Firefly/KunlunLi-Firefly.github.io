import { defineCollection } from "astro:content";
import type { CollectionConfig } from "astro/content/config";
import { glob } from "astro/loaders";
import { type ZodType, z } from "astro/zod";

type PostData = {
	title: string;
	published: Date;
	updated?: Date;
	draft: boolean;
	description: string;
	image: string;
	tags: string[];
	category: string | null;
	lang: string;
	pinned: boolean;
	author: string;
	sourceLink: string;
	licenseName: string;
	licenseUrl: string;
	comment: boolean;
	password: string;
	passwordHint: string;
	series: string;
	seriesOrder?: number;
	prevTitle: string;
	prevSlug: string;
	nextTitle: string;
	nextSlug: string;
};

type DynamicData = {
	published: Date;
	pinned: boolean;
	location: string;
};

type ProjectData = {
	title: string;
	summary: string;
	year: number;
	status: "completed" | "ongoing" | "coursework" | "manuscript";
	researchArea: string;
	methods: string[];
	datasets: string[];
	results: string[];
	role: string;
	collaborators: string[];
	featured: boolean;
	cover: string;
	sortOrder: number;
	links: {
		repository?: string;
		paper?: string;
		demo?: string;
		report?: string;
	};
};

type PublicationData = {
	title: string;
	authors: string[];
	year: number;
	venue: string;
	type: "conference" | "journal" | "preprint" | "manuscript";
	status: string;
	summary: string;
	doi: string;
	url: string;
	featured: boolean;
	sortOrder: number;
};

type ContentCollection<T> = CollectionConfig<
	ZodType<T>,
	ReturnType<typeof glob>
>;

const postsCollection: ContentCollection<PostData> = defineCollection({
	loader: glob({ pattern: "**/*.{md,mdx}", base: "./src/content/posts" }),
	schema: z.object({
		title: z.string(),
		published: z.date(),
		updated: z.date().optional(),
		draft: z.boolean().optional().default(false),
		description: z.string().optional().default(""),
		image: z.string().optional().default(""),
		tags: z.array(z.string()).optional().default([]),
		category: z.string().optional().nullable().default(""),
		lang: z.string().optional().default(""),
		pinned: z.boolean().optional().default(false),
		author: z.string().optional().default(""),
		sourceLink: z.string().optional().default(""),
		licenseName: z.string().optional().default(""),
		licenseUrl: z.string().optional().default(""),
		comment: z.boolean().optional().default(true),
		password: z.string().optional().default(""),
		passwordHint: z.string().optional().default(""),
		series: z.string().optional().default(""),
		seriesOrder: z.number().optional(),

		/* For internal use */
		prevTitle: z.string().default(""),
		prevSlug: z.string().default(""),
		nextTitle: z.string().default(""),
		nextSlug: z.string().default(""),
	}),
});

const specCollection: ContentCollection<Record<string, never>> =
	defineCollection({
		loader: glob({ pattern: "**/*.{md,mdx}", base: "./src/content/spec" }),
		schema: z.object({}),
	});

const dynamicCollection: ContentCollection<DynamicData> = defineCollection({
	loader: glob({ pattern: "**/*.md", base: "./src/content/dynamic" }),
	schema: z.object({
		published: z.date(),
		pinned: z.boolean().optional().default(false),
		location: z.string().optional().default(""),
	}),
});

const projectsCollection: ContentCollection<ProjectData> = defineCollection({
	loader: glob({ pattern: "**/*.{md,mdx}", base: "./src/content/projects" }),
	schema: z.object({
		title: z.string(),
		summary: z.string(),
		year: z.number(),
		status: z.enum(["completed", "ongoing", "coursework", "manuscript"]),
		researchArea: z.string(),
		methods: z.array(z.string()).default([]),
		datasets: z.array(z.string()).default([]),
		results: z.array(z.string()).default([]),
		role: z.string().default(""),
		collaborators: z.array(z.string()).default([]),
		featured: z.boolean().default(false),
		cover: z.string().default(""),
		sortOrder: z.number().default(0),
		links: z
			.object({
				repository: z.url().optional(),
				paper: z.url().optional(),
				demo: z.url().optional(),
				report: z.string().optional(),
			})
			.default({}),
	}),
});

const publicationsCollection: ContentCollection<PublicationData> =
	defineCollection({
		loader: glob({
			pattern: "**/*.{md,mdx}",
			base: "./src/content/publications",
		}),
		schema: z.object({
			title: z.string(),
			authors: z.array(z.string()),
			year: z.number(),
			venue: z.string(),
			type: z.enum(["conference", "journal", "preprint", "manuscript"]),
			status: z.string().default(""),
			summary: z.string().default(""),
			doi: z.string().default(""),
			url: z.url().or(z.literal("")),
			featured: z.boolean().default(false),
			sortOrder: z.number().default(0),
		}),
	});

export const collections: {
	dynamic: typeof dynamicCollection;
	posts: typeof postsCollection;
	projects: typeof projectsCollection;
	publications: typeof publicationsCollection;
	spec: typeof specCollection;
} = {
	dynamic: dynamicCollection,
	posts: postsCollection,
	projects: projectsCollection,
	publications: publicationsCollection,
	spec: specCollection,
};
