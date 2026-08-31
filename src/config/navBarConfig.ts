import {
	type NavBarConfig,
	type NavBarLink,
	type NavBarSearchConfig,
	NavBarSearchMethod,
} from "../types/navBarConfig";

const getDynamicNavBarConfig = (): NavBarConfig => ({
	links: [
		LinkPresets.Research,
		LinkPresets.Projects,
		LinkPresets.Publications,
		LinkPresets.Blog,
		LinkPresets.About,
		LinkPresets.GitHub,
	],
});

export const navBarSearchConfig: NavBarSearchConfig = {
	method: NavBarSearchMethod.PageFind,
};

export const LinkPresets: Record<string, NavBarLink> = {
	Research: {
		name: "Research",
		url: "/research/",
		icon: "material-symbols:science-outline",
	},
	Projects: {
		name: "Projects",
		url: "/projects/",
		icon: "material-symbols:work-outline",
	},
	Publications: {
		name: "Publications",
		url: "/publications/",
		icon: "material-symbols:article-outline",
	},
	Blog: {
		name: "Blog",
		url: "/blog/",
		icon: "material-symbols:edit-note-outline",
	},
	About: {
		name: "About",
		url: "/about/",
		icon: "material-symbols:person-outline",
	},
	GitHub: {
		name: "GitHub",
		url: "https://github.com/KunlunLi-Firefly",
		external: true,
		icon: "fa7-brands:github",
	},
};

export const navBarConfig: NavBarConfig = getDynamicNavBarConfig();
