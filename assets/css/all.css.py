@import url(font-awesome.min.css);
@import url("https://fonts.googleapis.com/css?family=Merriweather:300,700,300italic,700italic|Source+Sans+Pro:900");

/*
	Massively by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/

/* Reset */

	html, body, div, span, applet, object, iframe, h1, h2, h3, h4, h5, h6, p, blockquote, pre, a, abbr, acronym, address, big, cite, code, del, dfn, em, img, ins, kbd, q, s, samp, small, strike, strong, sub, sup, tt, var, b, u, i, center, dl, dt, dd, ol, ul, li, fieldset, form, label, legend, table, caption, tbody, tfoot, thead, tr, th, td, article, aside, canvas, details, embed, figure, figcaption, footer, header, hgroup, menu, nav, output, ruby, section, summary, time, mark, audio, video {
		margin: 0;
		padding: 0;
		border: 0;
		font-size: 100%;
		font: inherit;
		vertical-align: baseline;
	}

	article, aside, details, figcaption, figure, footer, header, hgroup, menu, nav, section {
		display: block;
	}

	body {
		line-height: 1;
	}

	ol, ul {
		list-style: none;
	}

	blockquote, q {
		quotes: none;
	}

	blockquote:before, blockquote:after, q:before, q:after {
		content: '';
		content: none;
	}

	table {
		border-collapse: collapse;
		border-spacing: 0;
	}

	body {
		-webkit-text-size-adjust: none;
	}

/* Box Model */

	*, *:before, *:after {
		-moz-box-sizing: border-box;
		-webkit-box-sizing: border-box;
		box-sizing: border-box;
	}

/* Grid */

	.row {
		border-bottom: solid 1px transparent;
		-moz-box-sizing: border-box;
		-webkit-box-sizing: border-box;
		box-sizing: border-box;
	}

	.row > * {
		float: left;
		-moz-box-sizing: border-box;
		-webkit-box-sizing: border-box;
		box-sizing: border-box;
	}

	.row:after, .row:before {
		content: '';
		display: block;
		clear: both;
		height: 0;
	}

	.row.uniform > * > :first-child {
		margin-top: 0;
	}

	.row.uniform > * > :last-child {
		margin-bottom: 0;
	}

	.row.\30 \25 > * {
		padding: 0 0 0 0rem;
	}

	.row.\30 \25 {
		margin: 0 0 -1px 0rem;
	}

	.row.uniform.\30 \25 > * {
		padding: 0rem 0 0 0rem;
	}

	.row.uniform.\30 \25 {
		margin: 0rem 0 -1px 0rem;
	}

	.row > * {
		padding: 0 0 0 1.5rem;
	}

	.row {
		margin: 0 0 -1px -1.5rem;
	}

	.row.uniform > * {
		padding: 1.5rem 0 0 1.5rem;
	}

	.row.uniform {
		margin: -1.5rem 0 -1px -1.5rem;
	}

	.row.\32 00\25 > * {
		padding: 0 0 0 3rem;
	}

	.row.\32 00\25 {
		margin: 0 0 -1px -3rem;
	}

	.row.uniform.\32 00\25 > * {
		padding: 3rem 0 0 3rem;
	}

	.row.uniform.\32 00\25 {
		margin: -3rem 0 -1px -3rem;
	}

	.row.\31 50\25 > * {
		padding: 0 0 0 2.25rem;
	}

	.row.\31 50\25 {
		margin: 0 0 -1px -2.25rem;
	}

	.row.uniform.\31 50\25 > * {
		padding: 2.25rem 0 0 2.25rem;
	}

	.row.uniform.\31 50\25 {
		margin: -2.25rem 0 -1px -2.25rem;
	}

	.row.\35 0\25 > * {
		padding: 0 0 0 0.75rem;
	}

	.row.\35 0\25 {
		margin: 0 0 -1px -0.75rem;
	}

	.row.uniform.\35 0\25 > * {
		padding: 0.75rem 0 0 0.75rem;
	}

	.row.uniform.\35 0\25 {
		margin: -0.75rem 0 -1px -0.75rem;
	}

	.row.\32 5\25 > * {
		padding: 0 0 0 0.375rem;
	}

	.row.\32 5\25 {
		margin: 0 0 -1px -0.375rem;
	}

	.row.uniform.\32 5\25 > * {
		padding: 0.375rem 0 0 0.375rem;
	}

	.row.uniform.\32 5\25 {
		margin: -0.375rem 0 -1px -0.375rem;
	}

	.\31 2u, .\31 2u\24 {
		width: 100%;
		clear: none;
		margin-left: 0;
	}

	.\31 1u, .\31 1u\24 {
		width: 91.6666666667%;
		clear: none;
		margin-left: 0;
	}

	.\31 0u, .\31 0u\24 {
		width: 83.3333333333%;
		clear: none;
		margin-left: 0;
	}

	.\39 u, .\39 u\24 {
		width: 75%;
		clear: none;
		margin-left: 0;
	}

	.\38 u, .\38 u\24 {
		width: 66.6666666667%;
		clear: none;
		margin-left: 0;
	}

	.\37 u, .\37 u\24 {
		width: 58.3333333333%;
		clear: none;
		margin-left: 0;
	}

	.\36 u, .\36 u\24 {
		width: 50%;
		clear: none;
		margin-left: 0;
	}

	.\35 u, .\35 u\24 {
		width: 41.6666666667%;
		clear: none;
		margin-left: 0;
	}

	.\34 u, .\34 u\24 {
		width: 33.3333333333%;
		clear: none;
		margin-left: 0;
	}

	.\33 u, .\33 u\24 {
		width: 25%;
		clear: none;
		margin-left: 0;
	}

	.\32 u, .\32 u\24 {
		width: 16.6666666667%;
		clear: none;
		margin-left: 0;
	}

	.\31 u, .\31 u\24 {
		width: 8.3333333333%;
		clear: none;
		margin-left: 0;
	}

	.\31 2u\24 + *,
	.\31 1u\24 + *,
	.\31 0u\24 + *,
	.\39 u\24 + *,
	.\38 u\24 + *,
	.\37 u\24 + *,
	.\36 u\24 + *,
	.\35 u\24 + *,
	.\34 u\24 + *,
	.\33 u\24 + *,
	.\32 u\24 + *,
	.\31 u\24 + * {
		clear: left;
	}

	.\-11u {
		margin-left: 91.66667%;
	}

	.\-10u {
		margin-left: 83.33333%;
	}

	.\-9u {
		margin-left: 75%;
	}

	.\-8u {
		margin-left: 66.66667%;
	}

	.\-7u {
		margin-left: 58.33333%;
	}

	.\-6u {
		margin-left: 50%;
	}

	.\-5u {
		margin-left: 41.66667%;
	}

	.\-4u {
		margin-left: 33.33333%;
	}

	.\-3u {
		margin-left: 25%;
	}

	.\-2u {
		margin-left: 16.66667%;
	}

	.\-1u {
		margin-left: 8.33333%;
	}

	@media screen and (max-width: 1680px) {

		.row > * {
			padding: 0 0 0 1.5rem;
		}

		.row {
			margin: 0 0 -1px -1.5rem;
		}

		.row.uniform > * {
			padding: 1.5rem 0 0 1.5rem;
		}

		.row.uniform {
			margin: -1.5rem 0 -1px -1.5rem;
		}

		.row.\32 00\25 > * {
			padding: 0 0 0 3rem;
		}

		.row.\32 00\25 {
			margin: 0 0 -1px -3rem;
		}

		.row.uniform.\32 00\25 > * {
			padding: 3rem 0 0 3rem;
		}

		.row.uniform.\32 00\25 {
			margin: -3rem 0 -1px -3rem;
		}

		.row.\31 50\25 > * {
			padding: 0 0 0 2.25rem;
		}

		.row.\31 50\25 {
			margin: 0 0 -1px -2.25rem;
		}

		.row.uniform.\31 50\25 > * {
			padding: 2.25rem 0 0 2.25rem;
		}

		.row.uniform.\31 50\25 {
			margin: -2.25rem 0 -1px -2.25rem;
		}

		.row.\35 0\25 > * {
			padding: 0 0 0 0.75rem;
		}

		.row.\35 0\25 {
			margin: 0 0 -1px -0.75rem;
		}

		.row.uniform.\35 0\25 > * {
			padding: 0.75rem 0 0 0.75rem;
		}

		.row.uniform.\35 0\25 {
			margin: -0.75rem 0 -1px -0.75rem;
		}

		.row.\32 5\25 > * {
			padding: 0 0 0 0.375rem;
		}

		.row.\32 5\25 {
			margin: 0 0 -1px -0.375rem;
		}

		.row.uniform.\32 5\25 > * {
			padding: 0.375rem 0 0 0.375rem;
		}

		.row.uniform.\32 5\25 {
			margin: -0.375rem 0 -1px -0.375rem;
		}

		.\31 2u\28xlarge\29, .\31 2u\24\28xlarge\29 {
			width: 100%;
			clear: none;
			margin-left: 0;
		}

		.\31 1u\28xlarge\29, .\31 1u\24\28xlarge\29 {
			width: 91.6666666667%;
			clear: none;
			margin-left: 0;
		}

		.\31 0u\28xlarge\29, .\31 0u\24\28xlarge\29 {
			width: 83.3333333333%;
			clear: none;
			margin-left: 0;
		}

		.\39 u\28xlarge\29, .\39 u\24\28xlarge\29 {
			width: 75%;
			clear: none;
			margin-left: 0;
		}

		.\38 u\28xlarge\29, .\38 u\24\28xlarge\29 {
			width: 66.6666666667%;
			clear: none;
			margin-left: 0;
		}

		.\37 u\28xlarge\29, .\37 u\24\28xlarge\29 {
			width: 58.3333333333%;
			clear: none;
			margin-left: 0;
		}

		.\36 u\28xlarge\29, .\36 u\24\28xlarge\29 {
			width: 50%;
			clear: none;
			margin-left: 0;
		}

		.\35 u\28xlarge\29, .\35 u\24\28xlarge\29 {
			width: 41.6666666667%;
			clear: none;
			margin-left: 0;
		}

		.\34 u\28xlarge\29, .\34 u\24\28xlarge\29 {
			width: 33.3333333333%;
			clear: none;
			margin-left: 0;
		}

		.\33 u\28xlarge\29, .\33 u\24\28xlarge\29 {
			width: 25%;
			clear: none;
			margin-left: 0;
		}

		.\32 u\28xlarge\29, .\32 u\24\28xlarge\29 {
			width: 16.6666666667%;
			clear: none;
			margin-left: 0;
		}

		.\31 u\28xlarge\29, .\31 u\24\28xlarge\29 {
			width: 8.3333333333%;
			clear: none;
			margin-left: 0;
		}

		.\31 2u\24\28xlarge\29 + *,
		.\31 1u\24\28xlarge\29 + *,
		.\31 0u\24\28xlarge\29 + *,
		.\39 u\24\28xlarge\29 + *,
		.\38 u\24\28xlarge\29 + *,
		.\37 u\24\28xlarge\29 + *,
		.\36 u\24\28xlarge\29 + *,
		.\35 u\24\28xlarge\29 + *,
		.\34 u\24\28xlarge\29 + *,
		.\33 u\24\28xlarge\29 + *,
		.\32 u\24\28xlarge\29 + *,
		.\31 u\24\28xlarge\29 + * {
			clear: left;
		}

		.\-11u\28xlarge\29 {
			margin-left: 91.66667%;
		}

		.\-10u\28xlarge\29 {
			margin-left: 83.33333%;
		}

		.\-9u\28xlarge\29 {
			margin-left: 75%;
		}

		.\-8u\28xlarge\29 {
			margin-left: 66.66667%;
		}

		.\-7u\28xlarge\29 {
			margin-left: 58.33333%;
		}

		.\-6u\28xlarge\29 {
			margin-left: 50%;
		}

		.\-5u\28xlarge\29 {
			margin-left: 41.66667%;
		}

		.\-4u\28xlarge\29 {
			margin-left: 33.33333%;
		}

		.\-3u\28xlarge\29 {
			margin-left: 25%;
		}

		.\-2u\28xlarge\29 {
			margin-left: 16.66667%;
		}

		.\-1u\28xlarge\29 {
			margin-left: 8.33333%;
		}

	}

	@media screen and (max-width: 1280px) {

		.row > * {
			padding: 0 0 0 1.5rem;
		}

		.row {
			margin: 0 0 -1px -1.5rem;
		}

		.row.uniform > * {
			padding: 1.5rem 0 0 1.5rem;
		}

		.row.uniform {
			margin: -1.5rem 0 -1px -1.5rem;
		}

		.row.\32 00\25 > * {
			padding: 0 0 0 3rem;
		}

		.row.\32 00\25 {
			margin: 0 0 -1px -3rem;
		}

		.row.uniform.\32 00\25 > * {
			padding: 3rem 0 0 3rem;
		}

		.row.uniform.\32 00\25 {
			margin: -3rem 0 -1px -3rem;
		}

		.row.\31 50\25 > * {
			padding: 0 0 0 2.25rem;
		}

		.row.\31 50\25 {
			margin: 0 0 -1px -2.25rem;
		}

		.row.uniform.\31 50\25 > * {
			padding: 2.25rem 0 0 2.25rem;
		}

		.row.uniform.\31 50\25 {
			margin: -2.25rem 0 -1px -2.25rem;
		}

		.row.\35 0\25 > * {
			padding: 0 0 0 0.75rem;
		}

		.row.\35 0\25 {
			margin: 0 0 -1px -0.75rem;
		}

		.row.uniform.\35 0\25 > * {
			padding: 0.75rem 0 0 0.75rem;
		}

		.row.uniform.\35 0\25 {
			margin: -0.75rem 0 -1px -0.75rem;
		}

		.row.\32 5\25 > * {
			padding: 0 0 0 0.375rem;
		}

		.row.\32 5\25 {
			margin: 0 0 -1px -0.375rem;
		}

		.row.uniform.\32 5\25 > * {
			padding: 0.375rem 0 0 0.375rem;
		}

		.row.uniform.\32 5\25 {
			margin: -0.375rem 0 -1px -0.375rem;
		}

		.\31 2u\28large\29, .\31 2u\24\28large\29 {
			width: 100%;
			clear: none;
			margin-left: 0;
		}

		.\31 1u\28large\29, .\31 1u\24\28large\29 {
			width: 91.6666666667%;
			clear: none;
			margin-left: 0;
		}

		.\31 0u\28large\29, .\31 0u\24\28large\29 {
			width: 83.3333333333%;
			clear: none;
			margin-left: 0;
		}

		.\39 u\28large\29, .\39 u\24\28large\29 {
			width: 75%;
			clear: none;
			margin-left: 0;
		}

		.\38 u\28large\29, .\38 u\24\28large\29 {
			width: 66.6666666667%;
			clear: none;
			margin-left: 0;
		}

		.\37 u\28large\29, .\37 u\24\28large\29 {
			width: 58.3333333333%;
			clear: none;
			margin-left: 0;
		}

		.\36 u\28large\29, .\36 u\24\28large\29 {
			width: 50%;
			clear: none;
			margin-left: 0;
		}

		.\35 u\28large\29, .\35 u\24\28large\29 {
			width: 41.6666666667%;
			clear: none;
			margin-left: 0;
		}

		.\34 u\28large\29, .\34 u\24\28large\29 {
			width: 33.3333333333%;
			clear: none;
			margin-left: 0;
		}

		.\33 u\28large\29, .\33 u\24\28large\29 {
			width: 25%;
			clear: none;
			margin-left: 0;
		}

		.\32 u\28large\29, .\32 u\24\28large\29 {
			width: 16.6666666667%;
			clear: none;
			margin-left: 0;
		}

		.\31 u\28large\29, .\31 u\24\28large\29 {
			width: 8.3333333333%;
			clear: none;
			margin-left: 0;
		}

		.\31 2u\24\28large\29 + *,
		.\31 1u\24\28large\29 + *,
		.\31 0u\24\28large\29 + *,
		.\39 u\24\28large\29 + *,
		.\38 u\24\28large\29 + *,
		.\37 u\24\28large\29 + *,
		.\36 u\24\28large\29 + *,
		.\35 u\24\28large\29 + *,
		.\34 u\24\28large\29 + *,
		.\33 u\24\28large\29 + *,
		.\32 u\24\28large\29 + *,
		.\31 u\24\28large\29 + * {
			clear: left;
		}

		.\-11u\28large\29 {
			margin-left: 91.66667%;
		}

		.\-10u\28large\29 {
			margin-left: 83.33333%;
		}

		.\-9u\28large\29 {
			margin-left: 75%;
		}

		.\-8u\28large\29 {
			margin-left: 66.66667%;
		}

		.\-7u\28large\29 {
			margin-left: 58.33333%;
		}

		.\-6u\28large\29 {
			margin-left: 50%;
		}

		.\-5u\28large\29 {
			margin-left: 41.66667%;
		}

		.\-4u\28large\29 {
			margin-left: 33.33333%;
		}

		.\-3u\28large\29 {
			margin-left: 25%;
		}

		.\-2u\28large\29 {
			margin-left: 16.66667%;
		}

		.\-1u\28large\29 {
			margin-left: 8.33333%;
		}

	}

	@media screen and (max-width: 980px) {

		.row > * {
			padding: 0 0 0 1.5rem;
		}

		.row {
			margin: 0 0 -1px -1.5rem;
		}

		.row.uniform > * {
			padding: 1.5rem 0 0 1.5rem;
		}

		.row.uniform {
			margin: -1.5rem 0 -1px -1.5rem;
		}

		.row.\32 00\25 > * {
			padding: 0 0 0 3rem;
		}

		.row.\32 00\25 {
			margin: 0 0 -1px -3rem;
		}

		.row.uniform.\32 00\25 > * {
			padding: 3rem 0 0 3rem;
		}

		.row.uniform.\32 00\25 {
			margin: -3rem 0 -1px -3rem;
		}

		.row.\31 50\25 > * {
			padding: 0 0 0 2.25rem;
		}

		.row.\31 50\25 {
			margin: 0 0 -1px -2.25rem;
		}

		.row.uniform.\31 50\25 > * {
			padding: 2.25rem 0 0 2.25rem;
		}

		.row.uniform.\31 50\25 {
			margin: -2.25rem 0 -1px -2.25rem;
		}

		.row.\35 0\25 > * {
			padding: 0 0 0 0.75rem;
		}

		.row.\35 0\25 {
			margin: 0 0 -1px -0.75rem;
		}

		.row.uniform.\35 0\25 > * {
			padding: 0.75rem 0 0 0.75rem;
		}

		.row.uniform.\35 0\25 {
			margin: -0.75rem 0 -1px -0.75rem;
		}

		.row.\32 5\25 > * {
			padding: 0 0 0 0.375rem;
		}

		.row.\32 5\25 {
			margin: 0 0 -1px -0.375rem;
		}

		.row.uniform.\32 5\25 > * {
			padding: 0.375rem 0 0 0.375rem;
		}

		.row.uniform.\32 5\25 {
			margin: -0.375rem 0 -1px -0.375rem;
		}

		.\31 2u\28medium\29, .\31 2u\24\28medium\29 {
			width: 100%;
			clear: none;
			margin-left: 0;
		}

		.\31 1u\28medium\29, .\31 1u\24\28medium\29 {
			width: 91.6666666667%;
			clear: none;
			margin-left: 0;
		}

		.\31 0u\28medium\29, .\31 0u\24\28medium\29 {
			width: 83.3333333333%;
			clear: none;
			margin-left: 0;
		}

		.\39 u\28medium\29, .\39 u\24\28medium\29 {
			width: 75%;
			clear: none;
			margin-left: 0;
		}

		.\38 u\28medium\29, .\38 u\24\28medium\29 {
			width: 66.6666666667%;
			clear: none;
			margin-left: 0;
		}

		.\37 u\28medium\29, .\37 u\24\28medium\29 {
			width: 58.3333333333%;
			clear: none;
			margin-left: 0;
		}

		.\36 u\28medium\29, .\36 u\24\28medium\29 {
			width: 50%;
			clear: none;
			margin-left: 0;
		}

		.\35 u\28medium\29, .\35 u\24\28medium\29 {
			width: 41.6666666667%;
			clear: none;
			margin-left: 0;
		}

		.\34 u\28medium\29, .\34 u\24\28medium\29 {
			width: 33.3333333333%;
			clear: none;
			margin-left: 0;
		}

		.\33 u\28medium\29, .\33 u\24\28medium\29 {
			width: 25%;
			clear: none;
			margin-left: 0;
		}

		.\32 u\28medium\29, .\32 u\24\28medium\29 {
			width: 16.6666666667%;
			clear: none;
			margin-left: 0;
		}

		.\31 u\28medium\29, .\31 u\24\28medium\29 {
			width: 8.3333333333%;
			clear: none;
			margin-left: 0;
		}

		.\31 2u\24\28medium\29 + *,
		.\31 1u\24\28medium\29 + *,
		.\31 0u\24\28medium\29 + *,
		.\39 u\24\28medium\29 + *,
		.\38 u\24\28medium\29 + *,
		.\37 u\24\28medium\29 + *,
		.\36 u\24\28medium\29 + *,
		.\35 u\24\28medium\29 + *,
		.\34 u\24\28medium\29 + *,
		.\33 u\24\28medium\29 + *,
		.\32 u\24\28medium\29 + *,
		.\31 u\24\28medium\29 + * {
			clear: left;
		}

		.\-11u\28medium\29 {
			margin-left: 91.66667%;
		}

		.\-10u\28medium\29 {
			margin-left: 83.33333%;
		}

		.\-9u\28medium\29 {
			margin-left: 75%;
		}

		.\-8u\28medium\29 {
			margin-left: 66.66667%;
		}

		.\-7u\28medium\29 {
			margin-left: 58.33333%;
		}

		.\-6u\28medium\29 {
			margin-left: 50%;
		}

		.\-5u\28medium\29 {
			margin-left: 41.66667%;
		}

		.\-4u\28medium\29 {
			margin-left: 33.33333%;
		}

		.\-3u\28medium\29 {
			margin-left: 25%;
		}

		.\-2u\28medium\29 {
			margin-left: 16.66667%;
		}

		.\-1u\28medium\29 {
			margin-left: 8.33333%;
		}

	}

	@media screen and (max-width: 736px) {

		.row > * {
			padding: 0 0 0 1.5rem;
		}

		.row {
			margin: 0 0 -1px -1.5rem;
		}

		.row.uniform > * {
			padding: 1.5rem 0 0 1.5rem;
		}

		.row.uniform {
			margin: -1.5rem 0 -1px -1.5rem;
		}

		.row.\32 00\25 > * {
			padding: 0 0 0 3rem;
		}

		.row.\32 00\25 {
			margin: 0 0 -1px -3rem;
		}

		.row.uniform.\32 00\25 > * {
			padding: 3rem 0 0 3rem;
		}

		.row.uniform.\32 00\25 {
			margin: -3rem 0 -1px -3rem;
		}

		.row.\31 50\25 > * {
			padding: 0 0 0 2.25rem;
		}

		.row.\31 50\25 {
			margin: 0 0 -1px -2.25rem;
		}

		.row.uniform.\31 50\25 > * {
			padding: 2.25rem 0 0 2.25rem;
		}

		.row.uniform.\31 50\25 {
			margin: -2.25rem 0 -1px -2.25rem;
		}

		.row.\35 0\25 > * {
			padding: 0 0 0 0.75rem;
		}

		.row.\35 0\25 {
			margin: 0 0 -1px -0.75rem;
		}

		.row.uniform.\35 0\25 > * {
			padding: 0.75rem 0 0 0.75rem;
		}

		.row.uniform.\35 0\25 {
			margin: -0.75rem 0 -1px -0.75rem;
		}

		.row.\32 5\25 > * {
			padding: 0 0 0 0.375rem;
		}

		.row.\32 5\25 {
			margin: 0 0 -1px -0.375rem;
		}

		.row.uniform.\32 5\25 > * {
			padding: 0.375rem 0 0 0.375rem;
		}

		.row.uniform.\32 5\25 {
			margin: -0.375rem 0 -1px -0.375rem;
		}

		.\31 2u\28small\29, .\31 2u\24\28small\29 {
			width: 100%;
			clear: none;
			margin-left: 0;
		}

		.\31 1u\28small\29, .\31 1u\24\28small\29 {
			width: 91.6666666667%;
			clear: none;
			margin-left: 0;
		}

		.\31 0u\28small\29, .\31 0u\24\28small\29 {
			width: 83.3333333333%;
			clear: none;
			margin-left: 0;
		}

		.\39 u\28small\29, .\39 u\24\28small\29 {
			width: 75%;
			clear: none;
			margin-left: 0;
		}

		.\38 u\28small\29, .\38 u\24\28small\29 {
			width: 66.6666666667%;
			clear: none;
			margin-left: 0;
		}

		.\37 u\28small\29, .\37 u\24\28small\29 {
			width: 58.3333333333%;
			clear: none;
			margin-left: 0;
		}

		.\36 u\28small\29, .\36 u\24\28small\29 {
			width: 50%;
			clear: none;
			margin-left: 0;
		}

		.\35 u\28small\29, .\35 u\24\28small\29 {
			width: 41.6666666667%;
			clear: none;
			margin-left: 0;
		}

		.\34 u\28small\29, .\34 u\24\28small\29 {
			width: 33.3333333333%;
			clear: none;
			margin-left: 0;
		}

		.\33 u\28small\29, .\33 u\24\28small\29 {
			width: 25%;
			clear: none;
			margin-left: 0;
		}

		.\32 u\28small\29, .\32 u\24\28small\29 {
			width: 16.6666666667%;
			clear: none;
			margin-left: 0;
		}

		.\31 u\28small\29, .\31 u\24\28small\29 {
			width: 8.3333333333%;
			clear: none;
			margin-left: 0;
		}

		.\31 2u\24\28small\29 + *,
		.\31 1u\24\28small\29 + *,
		.\31 0u\24\28small\29 + *,
		.\39 u\24\28small\29 + *,
		.\38 u\24\28small\29 + *,
		.\37 u\24\28small\29 + *,
		.\36 u\24\28small\29 + *,
		.\35 u\24\28small\29 + *,
		.\34 u\24\28small\29 + *,
		.\33 u\24\28small\29 + *,
		.\32 u\24\28small\29 + *,
		.\31 u\24\28small\29 + * {
			clear: left;
		}

		.\-11u\28small\29 {
			margin-left: 91.66667%;
		}

		.\-10u\28small\29 {
			margin-left: 83.33333%;
		}

		.\-9u\28small\29 {
			margin-left: 75%;
		}

		.\-8u\28small\29 {
			margin-left: 66.66667%;
		}

		.\-7u\28small\29 {
			margin-left: 58.33333%;
		}

		.\-6u\28small\29 {
			margin-left: 50%;
		}

		.\-5u\28small\29 {
			margin-left: 41.66667%;
		}

		.\-4u\28small\29 {
			margin-left: 33.33333%;
		}

		.\-3u\28small\29 {
			margin-left: 25%;
		}

		.\-2u\28small\29 {
			margin-left: 16.66667%;
		}

		.\-1u\28small\29 {
			margin-left: 8.33333%;
		}

	}

	@media screen and (max-width: 480px) {

		.row > * {
			padding: 0 0 0 1.5rem;
		}

		.row {
			margin: 0 0 -1px -1.5rem;
		}

		.row.uniform > * {
			padding: 1.5rem 0 0 1.5rem;
		}

		.row.uniform {
			margin: -1.5rem 0 -1px -1.5rem;
		}

		.row.\32 00\25 > * {
			padding: 0 0 0 3rem;
		}

		.row.\32 00\25 {
			margin: 0 0 -1px -3rem;
		}

		.row.uniform.\32 00\25 > * {
			padding: 3rem 0 0 3rem;
		}

		.row.uniform.\32 00\25 {
			margin: -3rem 0 -1px -3rem;
		}

		.row.\31 50\25 > * {
			padding: 0 0 0 2.25rem;
		}

		.row.\31 50\25 {
			margin: 0 0 -1px -2.25rem;
		}

		.row.uniform.\31 50\25 > * {
			padding: 2.25rem 0 0 2.25rem;
		}

		.row.uniform.\31 50\25 {
			margin: -2.25rem 0 -1px -2.25rem;
		}

		.row.\35 0\25 > * {
			padding: 0 0 0 0.75rem;
		}

		.row.\35 0\25 {
			margin: 0 0 -1px -0.75rem;
		}

		.row.uniform.\35 0\25 > * {
			padding: 0.75rem 0 0 0.75rem;
		}

		.row.uniform.\35 0\25 {
			margin: -0.75rem 0 -1px -0.75rem;
		}

		.row.\32 5\25 > * {
			padding: 0 0 0 0.375rem;
		}

		.row.\32 5\25 {
			margin: 0 0 -1px -0.375rem;
		}

		.row.uniform.\32 5\25 > * {
			padding: 0.375rem 0 0 0.375rem;
		}

		.row.uniform.\32 5\25 {
			margin: -0.375rem 0 -1px -0.375rem;
		}

		.\31 2u\28xsmall\29, .\31 2u\24\28xsmall\29 {
			width: 100%;
			clear: none;
			margin-left: 0;
		}

		.\31 1u\28xsmall\29, .\31 1u\24\28xsmall\29 {
			width: 91.6666666667%;
			clear: none;
			margin-left: 0;
		}

		.\31 0u\28xsmall\29, .\31 0u\24\28xsmall\29 {
			width: 83.3333333333%;
			clear: none;
			margin-left: 0;
		}

		.\39 u\28xsmall\29, .\39 u\24\28xsmall\29 {
			width: 75%;
			clear: none;
			margin-left: 0;
		}

		.\38 u\28xsmall\29, .\38 u\24\28xsmall\29 {
			width: 66.6666666667%;
			clear: none;
			margin-left: 0;
		}

		.\37 u\28xsmall\29, .\37 u\24\28xsmall\29 {
			width: 58.3333333333%;
			clear: none;
			margin-left: 0;
		}

		.\36 u\28xsmall\29, .\36 u\24\28xsmall\29 {
			width: 50%;
			clear: none;
			margin-left: 0;
		}

		.\35 u\28xsmall\29, .\35 u\24\28xsmall\29 {
			width: 41.6666666667%;
			clear: none;
			margin-left: 0;
		}

		.\34 u\28xsmall\29, .\34 u\24\28xsmall\29 {
			width: 33.3333333333%;
			clear: none;
			margin-left: 0;
		}

		.\33 u\28xsmall\29, .\33 u\24\28xsmall\29 {
			width: 25%;
			clear: none;
			margin-left: 0;
		}

		.\32 u\28xsmall\29, .\32 u\24\28xsmall\29 {
			width: 16.6666666667%;
			clear: none;
			margin-left: 0;
		}

		.\31 u\28xsmall\29, .\31 u\24\28xsmall\29 {
			width: 8.3333333333%;
			clear: none;
			margin-left: 0;
		}

		.\31 2u\24\28xsmall\29 + *,
		.\31 1u\24\28xsmall\29 + *,
		.\31 0u\24\28xsmall\29 + *,
		.\39 u\24\28xsmall\29 + *,
		.\38 u\24\28xsmall\29 + *,
		.\37 u\24\28xsmall\29 + *,
		.\36 u\24\28xsmall\29 + *,
		.\35 u\24\28xsmall\29 + *,
		.\34 u\24\28xsmall\29 + *,
		.\33 u\24\28xsmall\29 + *,
		.\32 u\24\28xsmall\29 + *,
		.\31 u\24\28xsmall\29 + * {
			clear: left;
		}

		.\-11u\28xsmall\29 {
			margin-left: 91.66667%;
		}

		.\-10u\28xsmall\29 {
			margin-left: 83.33333%;
		}

		.\-9u\28xsmall\29 {
			margin-left: 75%;
		}

		.\-8u\28xsmall\29 {
			margin-left: 66.66667%;
		}

		.\-7u\28xsmall\29 {
			margin-left: 58.33333%;
		}

		.\-6u\28xsmall\29 {
			margin-left: 50%;
		}

		.\-5u\28xsmall\29 {
			margin-left: 41.66667%;
		}

		.\-4u\28xsmall\29 {
			margin-left: 33.33333%;
		}

		.\-3u\28xsmall\29 {
			margin-left: 25%;
		}

		.\-2u\28xsmall\29 {
			margin-left: 16.66667%;
		}

		.\-1u\28xsmall\29 {
			margin-left: 8.33333%;
		}

	}

	@media screen and (max-width: 360px) {

		.row > * {
			padding: 0 0 0 1.5rem;
		}

		.row {
			margin: 0 0 -1px -1.5rem;
		}

		.row.uniform > * {
			padding: 1.5rem 0 0 1.5rem;
		}

		.row.uniform {
			margin: -1.5rem 0 -1px -1.5rem;
		}

		.row.\32 00\25 > * {
			padding: 0 0 0 3rem;
		}

		.row.\32 00\25 {
			margin: 0 0 -1px -3rem;
		}

		.row.uniform.\32 00\25 > * {
			padding: 3rem 0 0 3rem;
		}

		.row.uniform.\32 00\25 {
			margin: -3rem 0 -1px -3rem;
		}

		.row.\31 50\25 > * {
			padding: 0 0 0 2.25rem;
		}

		.row.\31 50\25 {
			margin: 0 0 -1px -2.25rem;
		}

		.row.uniform.\31 50\25 > * {
			padding: 2.25rem 0 0 2.25rem;
		}

		.row.uniform.\31 50\25 {
			margin: -2.25rem 0 -1px -2.25rem;
		}

		.row.\35 0\25 > * {
			padding: 0 0 0 0.75rem;
		}

		.row.\35 0\25 {
			margin: 0 0 -1px -0.75rem;
		}

		.row.uniform.\35 0\25 > * {
			padding: 0.75rem 0 0 0.75rem;
		}

		.row.uniform.\35 0\25 {
			margin: -0.75rem 0 -1px -0.75rem;
		}

		.row.\32 5\25 > * {
			padding: 0 0 0 0.375rem;
		}

		.row.\32 5\25 {
			margin: 0 0 -1px -0.375rem;
		}

		.row.uniform.\32 5\25 > * {
			padding: 0.375rem 0 0 0.375rem;
		}

		.row.uniform.\32 5\25 {
			margin: -0.375rem 0 -1px -0.375rem;
		}

		.\31 2u\28xxsmall\29, .\31 2u\24\28xxsmall\29 {
			width: 100%;
			clear: none;
			margin-left: 0;
		}

		.\31 1u\28xxsmall\29, .\31 1u\24\28xxsmall\29 {
			width: 91.6666666667%;
			clear: none;
			margin-left: 0;
		}

		.\31 0u\28xxsmall\29, .\31 0u\24\28xxsmall\29 {
			width: 83.3333333333%;
			clear: none;
			margin-left: 0;
		}

		.\39 u\28xxsmall\29, .\39 u\24\28xxsmall\29 {
			width: 75%;
			clear: none;
			margin-left: 0;
		}

		.\38 u\28xxsmall\29, .\38 u\24\28xxsmall\29 {
			width: 66.6666666667%;
			clear: none;
			margin-left: 0;
		}

		.\37 u\28xxsmall\29, .\37 u\24\28xxsmall\29 {
			width: 58.3333333333%;
			clear: none;
			margin-left: 0;
		}

		.\36 u\28xxsmall\29, .\36 u\24\28xxsmall\29 {
			width: 50%;
			clear: none;
			margin-left: 0;
		}

		.\35 u\28xxsmall\29, .\35 u\24\28xxsmall\29 {
			width: 41.6666666667%;
			clear: none;
			margin-left: 0;
		}

		.\34 u\28xxsmall\29, .\34 u\24\28xxsmall\29 {
			width: 33.3333333333%;
			clear: none;
			margin-left: 0;
		}

		.\33 u\28xxsmall\29, .\33 u\24\28xxsmall\29 {
			width: 25%;
			clear: none;
			margin-left: 0;
		}

		.\32 u\28xxsmall\29, .\32 u\24\28xxsmall\29 {
			width: 16.6666666667%;
			clear: none;
			margin-left: 0;
		}

		.\31 u\28xxsmall\29, .\31 u\24\28xxsmall\29 {
			width: 8.3333333333%;
			clear: none;
			margin-left: 0;
		}

		.\31 2u\24\28xxsmall\29 + *,
		.\31 1u\24\28xxsmall\29 + *,
		.\31 0u\24\28xxsmall\29 + *,
		.\39 u\24\28xxsmall\29 + *,
		.\38 u\24\28xxsmall\29 + *,
		.\37 u\24\28xxsmall\29 + *,
		.\36 u\24\28xxsmall\29 + *,
		.\35 u\24\28xxsmall\29 + *,
		.\34 u\24\28xxsmall\29 + *,
		.\33 u\24\28xxsmall\29 + *,
		.\32 u\24\28xxsmall\29 + *,
		.\31 u\24\28xxsmall\29 + * {
			clear: left;
		}

		.\-11u\28xxsmall\29 {
			margin-left: 91.66667%;
		}

		.\-10u\28xxsmall\29 {
			margin-left: 83.33333%;
		}

		.\-9u\28xxsmall\29 {
			margin-left: 75%;
		}

		.\-8u\28xxsmall\29 {
			margin-left: 66.66667%;
		}

		.\-7u\28xxsmall\29 {
			margin-left: 58.33333%;
		}

		.\-6u\28xxsmall\29 {
			margin-left: 50%;
		}

		.\-5u\28xxsmall\29 {
			margin-left: 41.66667%;
		}

		.\-4u\28xxsmall\29 {
			margin-left: 33.33333%;
		}

		.\-3u\28xxsmall\29 {
			margin-left: 25%;
		}

		.\-2u\28xxsmall\29 {
			margin-left: 16.66667%;
		}

		.\-1u\28xxsmall\29 {
			margin-left: 8.33333%;
		}

	}

/* Basic */

	@-ms-viewport {
		width: device-width;
	}

	body {
		-ms-overflow-style: scrollbar;
	}

	@media screen and (max-width: 480px) {

		html, body {
			min-width: 320px;
		}

	}

	body {
		background-color: #212931;
	}

		body.is-loading *, body.is-loading *:before, body.is-loading *:after {
			-moz-animation: none !important;
			-webkit-animation: none !important;
			-ms-animation: none !important;
			animation: none !important;
			-moz-transition: none !important;
			-webkit-transition: none !important;
			-ms-transition: none !important;
			transition: none !important;
		}

/* Type */

	html {
		font-size: 16pt;
	}

		@media screen and (max-width: 1680px) {

			html {
				font-size: 12pt;
			}

		}

		@media screen and (max-width: 1280px) {

			html {
				font-size: 11pt;
			}

		}

		@media screen and (max-width: 360px) {

			html {
				font-size: 10pt;
			}

		}

	body {
		color: #213b58;
	}

	body, input, select, textarea {
		font-family: "Merriweather", Georgia, serif;
		font-weight: 300;
		font-size: 1rem;
		line-height: 2.375;
	}

	a {
		-moz-transition: color 0.2s ease-in-out, background-color 0.2s ease-in-out, border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
		-webkit-transition: color 0.2s ease-in-out, background-color 0.2s ease-in-out, border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
		-ms-transition: color 0.2s ease-in-out, background-color 0.2s ease-in-out, border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
		transition: color 0.2s ease-in-out, background-color 0.2s ease-in-out, border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
		border-bottom: dotted 1px;
		text-decoration: none;
    
	}

		a:hover {
			border-bottom-color: transparent;
		}

	strong, b {
		font-weight: 600;
	}

	em, i {
		font-style: italic;
	}

	p {
		text-align: justify;
		margin: 0 0 2rem 0;
	}

	h1, h2, h3, h4, h5, h6 {
		font-family: "Source Sans Pro", Helvetica, sans-serif;
		font-weight: 900;
		line-height: 1.5;
		letter-spacing: 0.075em;
		text-transform: uppercase;
		margin: 0 0 1rem 0;
	}

		h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
			border-bottom: 0;
			color: inherit;
			text-decoration: none;
		}

	h1 {
		font-size: 4rem;
		line-height: 1.1;
		margin: 0 0 2rem 0;
	}

	h2 {
		font-size: 1.75rem;
		line-height: 1.3;
		margin: 0 0 1.5rem 0;
	}

	h3 {
		font-size: 1.25rem;
		margin: 0 0 1.5rem 0;
	}

	h4 {
		font-size: 1rem;
	}

	h5 {
		font-size: 0.9rem;
	}

	h6 {
		font-size: 0.8rem;
	}

	sub {
		font-size: 0.8rem;
		position: relative;
		top: 0.5rem;
	}

	sup {
		font-size: 0.8rem;
		position: relative;
		top: -0.5rem;
	}

	blockquote {
		border-left: solid 4px;
		font-style: italic;
		margin: 0 0 2rem 0;
		padding: 0.5rem 0 0.5rem 2rem;
	}

	code {
		border: solid 2px;
		font-family: "Courier New", monospace;
		font-size: 0.9rem;
		margin: 0 0.25rem;
		padding: 0.25rem 0.65rem;
	}

	pre {
		-webkit-overflow-scrolling: touch;
		font-family: "Courier New", monospace;
		font-size: 0.9rem;
		margin: 0 0 2rem 0;
	}

		pre code {
			display: block;
			line-height: 1.75;
			padding: 1rem 1.5rem;
			overflow-x: auto;
		}

	hr {
		border: 0;
		border-bottom: solid 2px;
		margin: 3rem 0;
	}

		hr.major {
			margin: 5rem 0;
		}

	.align-left {
		text-align: left;
	}

	.align-center {
		text-align: center;
	}

	.align-right {
		text-align: right;
	}

	input, select, textarea {
		color: #212931;
	}

	a {
		color: #0d5dab;
		border-bottom-color: rgba(33, 41, 49, 0.5);
	}

		a:hover {
			border-bottom-color: transparent;
			color: #213b58 !important;
		}

	strong, b {
		color: #212931;
	}

	h1, h2, h3, h4, h5, h6 {
		color: #212931;
	}

	blockquote {
		border-left-color: #eeeeee;
	}

	code {
		background: rgba(220, 220, 220, 0.25);
		border-color: #eeeeee;
	}

	hr {
		border-bottom-color: #eeeeee;
	}

/* Box */

	.box {
		border: solid 2px;
		margin-bottom: 2rem;
		padding: 1.5rem;
	}

		.box > :last-child,
		.box > :last-child > :last-child,
		.box > :last-child > :last-child > :last-child {
			margin-bottom: 0;
		}

		.box.alt {
			border: 0;
			border-radius: 0;
			padding: 0;
		}

	.box {
		border-color: #eeeeee;
	}

/* Button */

	input[type="submit"],
	input[type="reset"],
	input[type="button"],
	button,
	.button {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		-moz-transition: background-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out, color 0.2s ease-in-out;
		-webkit-transition: background-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out, color 0.2s ease-in-out;
		-ms-transition: background-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out, color 0.2s ease-in-out;
		transition: background-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out, color 0.2s ease-in-out;
		border: 0;
		cursor: pointer;
		display: inline-block;
		font-family: "Source Sans Pro", Helvetica, sans-serif;
		font-size: 0.8rem;
		font-weight: 900;
		letter-spacing: 0.075em;
		height: 3rem;
		line-height: 3rem;
		padding: 0 2rem;
		text-align: center;
		text-decoration: none;
		text-transform: uppercase;
		white-space: nowrap;
	}

		input[type="submit"].icon:before,
		input[type="reset"].icon:before,
		input[type="button"].icon:before,
		button.icon:before,
		.button.icon:before {
			margin-right: 0.5rem;
		}

		input[type="submit"].icon.solo,
		input[type="reset"].icon.solo,
		input[type="button"].icon.solo,
		button.icon.solo,
		.button.icon.solo {
			position: relative;
			width: 4rem;
			height: 4rem;
			line-height: 4rem;
			border-radius: 4rem;
			text-indent: 4rem;
			overflow: hidden;
			padding: 0;
			white-space: nowrap;
		}

			input[type="submit"].icon.solo:before,
			input[type="reset"].icon.solo:before,
			input[type="button"].icon.solo:before,
			button.icon.solo:before,
			.button.icon.solo:before {
				position: absolute;
				display: block;
				top: 0;
				left: 0;
				width: inherit;
				height: inherit;
				line-height: inherit;
				font-size: 1.25rem;
				margin-right: 0;
				text-align: center;
				text-indent: 0;
			}

		input[type="submit"].fit,
		input[type="reset"].fit,
		input[type="button"].fit,
		button.fit,
		.button.fit {
			display: block;
			margin: 0 0 1rem 0;
			width: 100%;
		}

		input[type="submit"].small,
		input[type="reset"].small,
		input[type="button"].small,
		button.small,
		.button.small {
			font-size: 0.7rem;
			height: 2.5rem;
			line-height: 2.5rem;
			padding: 0 1.5rem;
		}

		input[type="submit"].big,
		input[type="reset"].big,
		input[type="button"].big,
		button.big,
		.button.big {
			font-size: 0.9rem;
			height: 3.5rem;
			line-height: 3.5rem;
			padding: 0 2.75rem;
		}

		@media screen and (max-width: 980px) {

			input[type="submit"],
			input[type="reset"],
			input[type="button"],
			button,
			.button {
				font-size: 0.9rem;
				height: 3.25rem;
				line-height: 3.25rem;
			}

				input[type="submit"].big,
				input[type="reset"].big,
				input[type="button"].big,
				button.big,
				.button.big {
					font-size: 1rem;
					height: 3.75rem;
					line-height: 3.75rem;
				}

		}

		input[type="submit"].disabled, input[type="submit"]:disabled,
		input[type="reset"].disabled,
		input[type="reset"]:disabled,
		input[type="button"].disabled,
		input[type="button"]:disabled,
		button.disabled,
		button:disabled,
		.button.disabled,
		.button:disabled {
			-moz-pointer-events: none;
			-webkit-pointer-events: none;
			-ms-pointer-events: none;
			pointer-events: none;
			opacity: 0.25;
		}

	input[type="submit"],
	input[type="reset"],
	input[type="button"],
	button,
	.button {
		background-color: transparent;
		box-shadow: inset 0 0 0 2px #212931;
		color: #212931 !important;
	}

		input[type="submit"]:hover,
		input[type="reset"]:hover,
		input[type="button"]:hover,
		button:hover,
		.button:hover {
			box-shadow: inset 0 0 0 2px #18bfef;
			color: #18bfef !important;
		}

		input[type="submit"].special,
		input[type="reset"].special,
		input[type="button"].special,
		button.special,
		.button.special {
			background-color: #212931;
			box-shadow: none;
			color: #ffffff !important;
		}

			input[type="submit"].special:hover,
			input[type="reset"].special:hover,
			input[type="button"].special:hover,
			button.special:hover,
			.button.special:hover {
				background-color: #18bfef;
			}

/* Form */

	form {
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		-moz-flex-wrap: wrap;
		-webkit-flex-wrap: wrap;
		-ms-flex-wrap: wrap;
		flex-wrap: wrap;
		width: calc(100% + 3rem);
		margin: -1.5rem 0 2rem -1.5rem;
	}

		form > .field {
			-moz-flex-grow: 0;
			-webkit-flex-grow: 0;
			-ms-flex-grow: 0;
			flex-grow: 0;
			-moz-flex-shrink: 0;
			-webkit-flex-shrink: 0;
			-ms-flex-shrink: 0;
			flex-shrink: 0;
			padding: 1.5rem 0 0 1.5rem;
			width: calc(100% - 1.5rem);
		}

			form > .field.half {
				width: calc(50% - 0.75rem);
			}

			form > .field.third {
				width: calc(100%/3 - 0.5rem);
			}

			form > .field.quarter {
				width: calc(25% - 0.375rem);
			}

		form > .actions {
			-moz-flex-grow: 0;
			-webkit-flex-grow: 0;
			-ms-flex-grow: 0;
			flex-grow: 0;
			-moz-flex-shrink: 1;
			-webkit-flex-shrink: 1;
			-ms-flex-shrink: 1;
			flex-shrink: 1;
			margin: 1.875rem 0 0 1.5rem !important;
			width: calc(100% - 3rem);
		}

		form.alt {
			display: block;
			width: 100%;
			margin: 0 0 2rem 0;
		}

			form.alt > .actions {
				margin: 0 0 2rem 0;
				width: 100%;
			}

		@media screen and (max-width: 480px) {

			form {
				width: calc(100% + 3rem);
				margin: -1.5rem 0 2rem -1.5rem;
			}

				form > .field {
					padding: 1.5rem 0 0 1.5rem;
					width: calc(100% - 1.5rem);
				}

					form > .field.half {
						width: calc(100% - 1.5rem);
					}

					form > .field.third {
						width: calc(100% - 1.5rem);
					}

					form > .field.quarter {
						width: calc(100% - 1.5rem);
					}

				form > .actions {
					margin: 1.5rem 0 0 1.5rem;
					width: calc(100% - 3rem);
				}

		}

	label {
		display: block;
		font-family: "Source Sans Pro", Helvetica, sans-serif;
		font-weight: 900;
		line-height: 1.5;
		letter-spacing: 0.075em;
		font-size: 0.8rem;
		text-transform: uppercase;
		margin: 0 0 0.75rem 0;
	}

		@media screen and (max-width: 980px) {

			label {
				font-size: 0.9rem;
			}

		}

	input[type="text"],
	input[type="password"],
	input[type="email"],
	select,
	textarea {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		background: transparent;
		border: solid 2px;
		color: inherit;
		display: block;
		outline: 0;
		padding: 0 1rem;
		text-decoration: none;
		width: 100%;
	}

		input[type="text"]:invalid,
		input[type="password"]:invalid,
		input[type="email"]:invalid,
		select:invalid,
		textarea:invalid {
			box-shadow: none;
		}

	.select-wrapper {
		text-decoration: none;
		display: block;
		position: relative;
	}

		.select-wrapper:before {
			-moz-osx-font-smoothing: grayscale;
			-webkit-font-smoothing: antialiased;
			font-family: FontAwesome;
			font-style: normal;
			font-weight: normal;
			text-transform: none !important;
		}

		.select-wrapper:before {
			content: '\f078';
			display: block;
			height: 3rem;
			line-height: 3rem;
			pointer-events: none;
			position: absolute;
			right: 0;
			text-align: center;
			top: 0;
			width: 3rem;
		}

		.select-wrapper select::-ms-expand {
			display: none;
		}

	input[type="text"],
	input[type="password"],
	input[type="email"],
	select {
		height: 3rem;
	}

	textarea {
		padding: 0.75rem 1rem;
	}

	input[type="checkbox"],
	input[type="radio"] {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		display: block;
		float: left;
		margin-right: -2rem;
		opacity: 0;
		width: 1rem;
		z-index: -1;
	}

		input[type="checkbox"] + label,
		input[type="radio"] + label {
			text-decoration: none;
			cursor: pointer;
			display: inline-block;
			font-size: 1rem;
			letter-spacing: 0;
			font-family: "Merriweather", Georgia, serif;
			text-transform: none;
			font-weight: 300;
			padding-left: 2.8rem;
			padding-right: 1rem;
			position: relative;
		}

			input[type="checkbox"] + label:before,
			input[type="radio"] + label:before {
				-moz-osx-font-smoothing: grayscale;
				-webkit-font-smoothing: antialiased;
				font-family: FontAwesome;
				font-style: normal;
				font-weight: normal;
				text-transform: none !important;
			}

			input[type="checkbox"] + label:before,
			input[type="radio"] + label:before {
				border: solid 2px;
				content: '';
				display: inline-block;
				height: 1.8rem;
				left: 0;
				line-height: 1.725rem;
				position: absolute;
				text-align: center;
				top: -0.125rem;
				width: 1.8rem;
			}

		input[type="checkbox"]:checked + label:before,
		input[type="radio"]:checked + label:before {
			content: '\f00c';
		}

	input[type="radio"] + label:before {
		border-radius: 100%;
	}

	::-webkit-input-placeholder {
		opacity: 1.0;
	}

	:-moz-placeholder {
		opacity: 1.0;
	}

	::-moz-placeholder {
		opacity: 1.0;
	}

	:-ms-input-placeholder {
		opacity: 1.0;
	}

	.formerize-placeholder {
		opacity: 1.0;
	}

	label {
		color: #212931;
	}

	input[type="text"],
	input[type="password"],
	input[type="email"],
	select,
	textarea {
		border-color: #eeeeee;
	}

		input[type="text"]:focus,
		input[type="password"]:focus,
		input[type="email"]:focus,
		select:focus,
		textarea:focus {
			border-color: #18bfef;
		}

	select option {
		background-color: #ffffff;
		color: #212931;
	}

	.select-wrapper:before {
		color: #eeeeee;
	}

	input[type="checkbox"] + label,
	input[type="radio"] + label {
		color: #212931;
	}

		input[type="checkbox"] + label:before,
		input[type="radio"] + label:before {
			border-color: #eeeeee;
		}

	input[type="checkbox"]:checked + label:before,
	input[type="radio"]:checked + label:before {
		background-color: #212931;
		border-color: #212931;
		color: #ffffff;
	}

	input[type="checkbox"]:focus + label:before,
	input[type="radio"]:focus + label:before {
		border-color: #18bfef;
	}

	::-webkit-input-placeholder {
		color: #909498 !important;
	}

	:-moz-placeholder {
		color: #909498 !important;
	}

	::-moz-placeholder {
		color: #909498 !important;
	}

	:-ms-input-placeholder {
		color: #909498 !important;
	}

	.formerize-placeholder {
		color: #909498 !important;
	}

/* Icon */

	.icon {
		text-decoration: none;
		border-bottom: none;
		position: relative;
	}

		.icon:before {
			-moz-osx-font-smoothing: grayscale;
			-webkit-font-smoothing: antialiased;
			font-family: FontAwesome;
			font-style: normal;
			font-weight: normal;
			text-transform: none !important;
		}

		.icon > .label {
			display: none;
		}

/* Image */

	.image {
		border: 0;
		display: inline-block;
		position: relative;
	}

		.image img {
			display: block;
		}

		.image.left, .image.right {
			max-width: 40%;
		}

			.image.left img, .image.right img {
				width: 100%;
			}

		.image.left {
			float: left;
			margin: 0 2rem 2rem 0;
			top: 0.75rem;
		}

		.image.right {
			float: right;
			margin: 0 0 2rem 2rem;
			top: 0.75rem;
		}

		.image.fit {
			display: block;
			margin: 2.5rem 0;
			width: 100%;
		}

			.image.fit:first-child {
				margin-top: 0;
			}

			.image.fit img {
				width: 100%;
			}

		.image.main {
			display: block;
			margin: 4rem 0;
			width: 100%;
		}

			.image.main:first-child {
				margin-top: 0;
			}

			.image.main img {
				width: 100%;
			}

		@media screen and (max-width: 736px) {

			.image.fit {
				margin: 2rem 0;
			}

			.image.main {
				margin: 2rem 0;
			}

		}

	a.image {
		overflow: hidden;
	}

		a.image img {
			-moz-transition: -moz-transform 0.2s ease-out;
			-webkit-transition: -webkit-transform 0.2s ease-out;
			-ms-transition: -ms-transform 0.2s ease-out;
			transition: transform 0.2s ease-out;
		}

		a.image:hover img {
			-moz-transform: scale(1.05);
			-webkit-transform: scale(1.05);
			-ms-transform: scale(1.05);
			transform: scale(1.05);
		}

/* List */

	ol {
		list-style: decimal;
		margin: 0 0 2rem 0;
		padding-left: 1.25rem;
	}

		ol li {
			padding-left: 0.25rem;
		}

	ul {
		list-style: disc;
		margin: 0 0 2rem 0;
		padding-left: 1rem;
	}

		ul li {
			padding-left: 0.5rem;
		}

		ul.divided {
			list-style: none;
			padding-left: 0;
		}

			ul.divided li {
				border-top: solid 1px;
				padding: 0.5rem 0;
			}

				ul.divided li:first-child {
					border-top: 0;
					padding-top: 0;
				}

		ul.icons {
			cursor: default;
			list-style: none;
			padding-left: 0;
		}

			ul.icons li {
				display: inline-block;
				padding: 0 0.5rem 0 0;
				vertical-align: middle;
			}

				ul.icons li:last-child {
					padding-right: 0;
				}

				ul.icons li .icon:before {
					width: 2.25rem;
					height: 2.25rem;
					line-height: 2.25rem;
					display: inline-block;
					text-align: center;
					border-radius: 100%;
					font-size: 1.25rem;
				}

			ul.icons.alt li .icon:before {
				-moz-transition: color 0.2s ease-in-out, background-color 0.2s ease-in-out, border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
				-webkit-transition: color 0.2s ease-in-out, background-color 0.2s ease-in-out, border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
				-ms-transition: color 0.2s ease-in-out, background-color 0.2s ease-in-out, border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
				transition: color 0.2s ease-in-out, background-color 0.2s ease-in-out, border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
				font-size: 1rem;
			}

		ul.actions {
			cursor: default;
			list-style: none;
			padding-left: 0;
		}

			ul.actions li {
				display: inline-block;
				padding: 0 1rem 0 0;
				vertical-align: middle;
			}

				ul.actions li:last-child {
					padding-right: 0;
				}

			ul.actions.small li {
				padding: 0 0.5rem 0 0;
			}

			ul.actions.vertical li {
				display: block;
				padding: 1rem 0 0 0;
			}

				ul.actions.vertical li:first-child {
					padding-top: 0;
				}

				ul.actions.vertical li > * {
					margin-bottom: 0;
				}

			ul.actions.vertical.small li {
				padding: 0.5rem 0 0 0;
			}

				ul.actions.vertical.small li:first-child {
					padding-top: 0;
				}

			ul.actions.fit {
				display: table;
				margin-left: -1rem;
				padding: 0;
				table-layout: fixed;
				width: calc(100% + 1rem);
			}

				ul.actions.fit li {
					display: table-cell;
					padding: 0 0 0 1rem;
				}

					ul.actions.fit li > * {
						margin-bottom: 0;
					}

				ul.actions.fit.small {
					margin-left: -0.5rem;
					width: calc(100% + 0.5rem);
				}

					ul.actions.fit.small li {
						padding: 0 0 0 0.5rem;
					}

			@media screen and (max-width: 480px) {

				ul.actions {
					margin: 0 0 2rem 0;
				}

					ul.actions li {
						padding: 1rem 0 0 0;
						display: block;
						text-align: center;
						width: 100%;
					}

						ul.actions li:first-child {
							padding-top: 0;
						}

						ul.actions li > * {
							width: 100%;
							margin: 0 !important;
						}

							ul.actions li > *.icon:before {
								margin-left: -2rem;
							}

					ul.actions.small li {
						padding: 0.5rem 0 0 0;
					}

						ul.actions.small li:first-child {
							padding-top: 0;
						}

			}

	dl {
		margin: 0 0 2rem 0;
	}

		dl dt {
			display: block;
			font-weight: 600;
			margin: 0 0 1rem 0;
		}

		dl dd {
			margin-left: 2rem;
		}

	ul.divided li {
		border-top-color: #eeeeee;
	}

	ul.icons li a.icon:hover:before {
		color: #18bfef;
	}

	ul.icons.alt li .icon:before {
		box-shadow: inset 0 0 0 2px #eeeeee;
	}

	ul.icons.alt li a.icon:hover:before {
		box-shadow: inset 0 0 0 2px #18bfef;
	}

/* Section/Article */

	section.special, article.special {
		text-align: center;
	}

	header {
		cursor: default;
	}

		header > .date {
			display: block;
			font-size: 0.8rem;
			height: 1;
			margin: 0 0 1rem 0;
			position: relative;
		}

		header > p {
			font-style: italic;
		}

		header > h1 + p {
			font-size: 1.1rem;
			margin-top: -0.5rem;
			line-height: 2;
		}

		header > h2 + p {
			font-size: 1rem;
			margin-top: -0.75rem;
		}

		header > h3 + p {
			font-size: 0.9rem;
			margin-top: -0.75rem;
		}

		header > h4 + p {
			font-size: 0.8rem;
			margin-top: -0.75rem;
		}

		header.major {
			margin: 0 0 4rem 0;
			text-align: center;
		}

			header.major > :last-child {
				margin-bottom: 0;
			}

			header.major > p {
				margin-top: 0;
				text-align: center;
			}

			header.major > .date {
				font-size: 1rem;
				margin: 0 0 4rem 0;
			}

				header.major > .date:before, header.major > .date:after {
					content: '';
					display: block;
					position: absolute;
					top: 50%;
					width: calc(50% - 6rem);
					border-top: solid 2px;
				}

				header.major > .date:before {
					left: 0;
				}

				header.major > .date:after {
					right: 0;
				}

		@media screen and (max-width: 980px) {

			header br {
				display: none;
			}

		}

		@media screen and (max-width: 736px) {

			header.major {
				margin: 0 0 2rem 0;
			}

		}

	header.major .date:before, header.major .date:after {
		border-top-color: #eeeeee;
	}

/* Table */

	.table-wrapper {
		-webkit-overflow-scrolling: touch;
		overflow-x: auto;
	}

	table {
		margin: 0 0 2rem 0;
		width: 100%;
	}

		table tbody tr {
			border: solid 1px;
			border-left: 0;
			border-right: 0;
		}

		table td {
			padding: 0.75rem 0.75rem;
		}

		table th {
			font-family: "Source Sans Pro", Helvetica, sans-serif;
			font-size: 0.8rem;
			font-weight: 900;
			letter-spacing: 0.075em;
			line-height: 1.5;
			padding: 0 0.75rem 0.75rem 0.75rem;
			text-align: left;
			text-transform: uppercase;
		}

			@media screen and (max-width: 980px) {

				table th {
					font-size: 0.9rem;
				}

			}

		table thead {
			border-bottom: solid 2px;
		}

		table tfoot {
			border-top: solid 2px;
		}

		table.alt {
			border-collapse: separate;
		}

			table.alt tbody tr td {
				border: solid 1px;
				border-left-width: 0;
				border-top-width: 0;
			}

				table.alt tbody tr td:first-child {
					border-left-width: 1px;
				}

			table.alt tbody tr:first-child td {
				border-top-width: 1px;
			}

			table.alt thead {
				border-bottom: 0;
			}

			table.alt tfoot {
				border-top: 0;
			}

	table tbody tr {
		border-color: #eeeeee;
	}

		table tbody tr:nth-child(2n + 1) {
			background-color: rgba(220, 220, 220, 0.25);
		}

	table th {
		color: #212931;
	}

	table thead {
		border-bottom-color: #eeeeee;
	}

	table tfoot {
		border-top-color: #eeeeee;
	}

	table.alt tbody tr td {
		border-color: #eeeeee;
	}

/* Pagination */

	.pagination {
		display: inline-flex;
		-moz-user-select: none;
		-webkit-user-select: none;
		-ms-user-select: none;
		user-select: none;
		cursor: default;
		list-style: none;
		margin: 0 0 2rem 2px;
		padding: 0;
	}

		.pagination a, .pagination span {
			-moz-transition: background-color 0.2s ease-in-out, border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out, color 0.2s ease-in-out;
			-webkit-transition: background-color 0.2s ease-in-out, border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out, color 0.2s ease-in-out;
			-ms-transition: background-color 0.2s ease-in-out, border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out, color 0.2s ease-in-out;
			transition: background-color 0.2s ease-in-out, border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out, color 0.2s ease-in-out;
			border: solid 2px;
			display: inline-block;
			font-family: "Source Sans Pro", Helvetica, sans-serif;
			font-size: 0.8rem;
			font-weight: 900;
			height: 3rem;
			letter-spacing: 0.075em;
			line-height: calc(3rem - 4px);
			margin-left: -2px;
			min-width: 3rem;
			position: relative;
			text-align: center;
			text-decoration: none;
			text-transform: uppercase;
		}

		.pagination .next, .pagination .previous {
			text-decoration: none;
			padding: 0 1.75rem;
		}

			.pagination .next:before, .pagination .previous:before {
				-moz-osx-font-smoothing: grayscale;
				-webkit-font-smoothing: antialiased;
				font-family: FontAwesome;
				font-style: normal;
				font-weight: normal;
				text-transform: none !important;
			}

			.pagination .next:before, .pagination .previous:before {
				display: inline-block;
				color: inherit !important;
			}

		.pagination .previous:before {
			content: '\f104';
			margin-right: 0.9375em;
		}

		.pagination .next:before {
			content: '\f105';
			float: right;
			margin-left: 0.9375em;
		}

		@media screen and (max-width: 980px) {

			.pagination a, .pagination span {
				font-size: 0.9rem;
			}

		}

		@media screen and (max-width: 480px) {

			.pagination .page, .pagination .extra {
				display: none;
			}

		}

	.pagination a, .pagination span {
		border-color: #eeeeee;
	}

	.pagination a {
		color: #212931 !important;
	}

		.pagination a:hover {
			color: #18bfef !important;
			border-color: #18bfef;
			z-index: 1;
		}

			.pagination a:hover + a, .pagination a:hover + span {
				border-left-color: #18bfef;
			}

		.pagination a.active {
			background-color: #eeeeee;
		}

	.pagination span {
		color: #eeeeee;
	}

/* Wrapper */

	#wrapper {
		-moz-transition: opacity 0.5s ease;
		-webkit-transition: opacity 0.5s ease;
		-ms-transition: opacity 0.5s ease;
		transition: opacity 0.5s ease;
		position: relative;
		z-index: 1;
		overflow: hidden;
	}

		#wrapper > .bg {
			position: absolute;
			top: 0;
			left: 0;
			width: 100%;
			height: 100%;
			background-color: #212931;
			background-image: url("../../images/overlay.png"), linear-gradient(0deg, rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.1)), url("../../images/bg.jpg");
			background-size: auto,								auto,														100% auto;
			background-position: center,								center,														top center;
			background-repeat: repeat,								no-repeat,													no-repeat;
			background-attachment: scroll,								scroll,														scroll;
			z-index: -1;
		}

			#wrapper > .bg.fixed {
				position: fixed;
				width: 100vw;
				height: 100vh;
			}

		#wrapper.fade-in:before {
			-moz-pointer-events: none;
			-webkit-pointer-events: none;
			-ms-pointer-events: none;
			pointer-events: none;
			-moz-transition: opacity 1s ease-in-out;
			-webkit-transition: opacity 1s ease-in-out;
			-ms-transition: opacity 1s ease-in-out;
			transition: opacity 1s ease-in-out;
			-moz-transition-delay: 0.75s;
			-webkit-transition-delay: 0.75s;
			-ms-transition-delay: 0.75s;
			transition-delay: 0.75s;
			background: #1e252d;
			content: '';
			display: block;
			height: 100%;
			left: 0;
			opacity: 0;
			position: fixed;
			top: 0;
			width: 100%;
		}

		body.is-loading #wrapper.fade-in:before {
			opacity: 1;
		}

		@media screen and (orientation: portrait) {

			#wrapper > .bg {
				background-size: auto,								auto,														auto 175%;
			}

		}

/* Intro */

	#intro {
		color: #ffffff;
		padding: 8rem 4rem 6rem 4rem ;
		-moz-align-items: center;
		-webkit-align-items: center;
		-ms-align-items: center;
		align-items: center;
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		-moz-flex-direction: column;
		-webkit-flex-direction: column;
		-ms-flex-direction: column;
		flex-direction: column;
		-moz-justify-content: -moz-flex-end;
		-webkit-justify-content: -webkit-flex-end;
		-ms-justify-content: -ms-flex-end;
		justify-content: flex-end;
		-moz-transition: opacity 1s ease, -moz-transform 1s ease;
		-webkit-transition: opacity 1s ease, -webkit-transform 1s ease;
		-ms-transition: opacity 1s ease, -ms-transform 1s ease;
		transition: opacity 1s ease, transform 1s ease;
		position: relative;
		cursor: default;
		text-align: center;
		z-index: 1;
		min-height: 100vh;
	}

		#intro input, #intro select, #intro textarea {
			color: #ffffff;
		}

		#intro a {
			color: #ffffff;
			border-bottom-color: rgba(255, 255, 255, 0.5);
		}

			#intro a:hover {
				border-bottom-color: transparent;
				color: #18bfef !important;
			}

		#intro strong, #intro b {
			color: #ffffff;
		}

		#intro h1, #intro h2, #intro h3, #intro h4, #intro h5, #intro h6 {
			color: #ffffff;
		}

		#intro blockquote {
			border-left-color: #ffffff;
		}

		#intro code {
			background: rgba(255, 255, 255, 0.075);
			border-color: #ffffff;
		}

		#intro hr {
			border-bottom-color: #ffffff;
		}

		#intro input[type="submit"],
		#intro input[type="reset"],
		#intro input[type="button"],
		#intro button,
		#intro .button {
			background-color: transparent;
			box-shadow: inset 0 0 0 2px #ffffff;
			color: #ffffff !important;
		}

			#intro input[type="submit"]:hover,
			#intro input[type="reset"]:hover,
			#intro input[type="button"]:hover,
			#intro button:hover,
			#intro .button:hover {
				box-shadow: inset 0 0 0 2px #18bfef;
				color: #18bfef !important;
			}

			#intro input[type="submit"].special,
			#intro input[type="reset"].special,
			#intro input[type="button"].special,
			#intro button.special,
			#intro .button.special {
				background-color: #ffffff;
				box-shadow: none;
				color: #1e252d !important;
			}

				#intro input[type="submit"].special:hover,
				#intro input[type="reset"].special:hover,
				#intro input[type="button"].special:hover,
				#intro button.special:hover,
				#intro .button.special:hover {
					background-color: #18bfef;
				}

		#intro h1 {
			font-size: 5rem;
			line-height: 1;
		}

		#intro p {
			font-size: 1.25rem;
			font-style: italic;
			margin-top: -0.25rem;
			text-align: center;
		}

		#intro + #header {
			margin-top: -20rem;
		}

			#intro + #header .logo {
				-moz-transform: translateY(2rem);
				-webkit-transform: translateY(2rem);
				-ms-transform: translateY(2rem);
				transform: translateY(2rem);
				opacity: 0;
				visibility: hidden;
			}

		#intro.hidden {
			-moz-pointer-events: none;
			-webkit-pointer-events: none;
			-ms-pointer-events: none;
			pointer-events: none;
			-moz-transform: translateY(2rem);
			-webkit-transform: translateY(2rem);
			-ms-transform: translateY(2rem);
			transform: translateY(2rem);
			-moz-transition: opacity 0.5s ease, -moz-transform 0.5s ease, visibility 0.5s;
			-webkit-transition: opacity 0.5s ease, -webkit-transform 0.5s ease, visibility 0.5s;
			-ms-transition: opacity 0.5s ease, -ms-transform 0.5s ease, visibility 0.5s;
			transition: opacity 0.5s ease, transform 0.5s ease, visibility 0.5s;
			opacity: 0;
			visibility: hidden;
		}

			#intro.hidden + #header .logo {
				-moz-transform: translateY(0);
				-webkit-transform: translateY(0);
				-ms-transform: translateY(0);
				transform: translateY(0);
				opacity: 1;
				visibility: visible;
			}

		body.is-loading #intro {
			-moz-transform: translateY(2rem);
			-webkit-transform: translateY(2rem);
			-ms-transform: translateY(2rem);
			transform: translateY(2rem);
			opacity: 0;
		}

			body.is-loading #intro:not(.hidden) + #header + #nav {
				-moz-transform: translateY(4rem);
				-webkit-transform: translateY(4rem);
				-ms-transform: translateY(4rem);
				transform: translateY(4rem);
				opacity: 0;
			}

		@media screen and (max-width: 980px) {

			#intro {
				padding: 4rem 4rem 2rem 4rem ;
				min-height: 90vh;
			}

				#intro p br {
					display: none;
				}

				#intro + #header {
					margin-top: -14rem;
				}

		}

		@media screen and (max-width: 736px) {

			#intro {
				padding: 3rem 2rem 1rem 2rem ;
				min-height: 80vh;
			}

				#intro h1 {
					font-size: 3.25rem;
					line-height: 1.1;
					margin-bottom: 1rem;
				}

				#intro p {
					font-size: 1rem;
					margin-top: 0rem;
				}

				#intro .actions {
					display: none;
				}

		}

/* Header */

	#header {
		color: #ffffff;
		-moz-align-items: center;
		-webkit-align-items: center;
		-ms-align-items: center;
		align-items: center;
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		-moz-flex-direction: column;
		-webkit-flex-direction: column;
		-ms-flex-direction: column;
		flex-direction: column;
		-moz-justify-content: -moz-flex-end;
		-webkit-justify-content: -webkit-flex-end;
		-ms-justify-content: -ms-flex-end;
		justify-content: flex-end;
		-moz-pointer-events: none;
		-webkit-pointer-events: none;
		-ms-pointer-events: none;
		pointer-events: none;
		-moz-user-select: none;
		-webkit-user-select: none;
		-ms-user-select: none;
		user-select: none;
		height: 20rem;
		padding-bottom: 8rem;
		position: relative;
		text-align: center;
		z-index: 2;
	}

		#header input, #header select, #header textarea {
			color: #ffffff;
		}

		#header a {
			color: #ffffff;
			border-bottom-color: rgba(255, 255, 255, 0.5);
		}

			#header a:hover {
				border-bottom-color: transparent;
				color: #18bfef !important;
			}

		#header strong, #header b {
			color: #ffffff;
		}

		#header h1, #header h2, #header h3, #header h4, #header h5, #header h6 {
			color: #ffffff;
		}

		#header blockquote {
			border-left-color: #ffffff;
		}

		#header code {
			background: rgba(255, 255, 255, 0.075);
			border-color: #ffffff;
		}

		#header hr {
			border-bottom-color: #ffffff;
		}

		#header .logo {
			-moz-transition: border-color 0.2s ease-in-out, color 0.2s ease-in-out, opacity 0.5s ease, -moz-transform 0.5s ease, visibility 0.5s;
			-webkit-transition: border-color 0.2s ease-in-out, color 0.2s ease-in-out, opacity 0.5s ease, -webkit-transform 0.5s ease, visibility 0.5s;
			-ms-transition: border-color 0.2s ease-in-out, color 0.2s ease-in-out, opacity 0.5s ease, -ms-transform 0.5s ease, visibility 0.5s;
			transition: border-color 0.2s ease-in-out, color 0.2s ease-in-out, opacity 0.5s ease, transform 0.5s ease, visibility 0.5s;
			-moz-pointer-events: auto;
			-webkit-pointer-events: auto;
			-ms-pointer-events: auto;
			pointer-events: auto;
			border-style: solid;
			border-color: #ffffff;
			border-width: 5px !important;
			font-family: "Source Sans Pro", Helvetica, sans-serif;
			font-size: 2.25rem;
			font-weight: 900;
			letter-spacing: 0.075em;
			line-height: 1;
			padding: 1rem 1.75rem;
			text-transform: uppercase;
			visibility: visible;
		}

			#header .logo:hover {
				border-color: #18bfef !important;
				color: #18bfef !important;
			}

		@media screen and (max-width: 980px) {

			#header {
				height: 14rem;
				padding-bottom: 4rem;
			}

		}

		@media screen and (max-width: 736px) {

			#header {
				padding-bottom: 3rem;
			}

				#header .logo {
					font-size: 1.75rem;
					border-width: 3px !important;
				}

		}

/* Nav */

	#nav {
		color: #ffffff;
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		-moz-transition: -moz-transform 1s ease, opacity 1s ease;
		-webkit-transition: -webkit-transform 1s ease, opacity 1s ease;
		-ms-transition: -ms-transform 1s ease, opacity 1s ease;
		transition: transform 1s ease, opacity 1s ease;
		background: rgba(255, 255, 255, 0.175);
		height: 4rem;
		line-height: 4rem;
		margin: -4rem auto 0 auto;
		overflow: hidden;
		padding: 0 2rem 0 0;
		position: relative;
		width: calc(100% - 4rem);
		max-width: 72rem;
		z-index: 2;
	}

		#nav ul.divided li {
			border-top-color: #ffffff;
		}

		#nav ul.icons li a.icon:hover:before {
			color: #18bfef;
		}

		#nav ul.icons.alt li .icon:before {
			box-shadow: inset 0 0 0 2px #ffffff;
		}

		#nav ul.icons.alt li a.icon:hover:before {
			box-shadow: inset 0 0 0 2px #18bfef;
		}

		#nav input, #nav select, #nav textarea {
			color: #ffffff;
		}

		#nav a {
			color: #ffffff;
			border-bottom-color: rgba(255, 255, 255, 0.5);
		}

			#nav a:hover {
				border-bottom-color: transparent;
				color: #18bfef !important;
			}

		#nav strong, #nav b {
			color: #ffffff;
		}

		#nav h1, #nav h2, #nav h3, #nav h4, #nav h5, #nav h6 {
			color: #ffffff;
		}

		#nav blockquote {
			border-left-color: #ffffff;
		}

		#nav code {
			background: rgba(255, 255, 255, 0.075);
			border-color: #ffffff;
		}

		#nav hr {
			border-bottom-color: #ffffff;
		}

		#nav ul.links {
			display: -moz-flex;
			display: -webkit-flex;
			display: -ms-flex;
			display: flex;
			-moz-flex-grow: 1;
			-webkit-flex-grow: 1;
			-ms-flex-grow: 1;
			flex-grow: 1;
			-moz-flex-shrink: 1;
			-webkit-flex-shrink: 1;
			-ms-flex-shrink: 1;
			flex-shrink: 1;
			font-family: "Source Sans Pro", Helvetica, sans-serif;
			font-weight: 900;
			color: #002b55
			letter-spacing: 0.075em;
			list-style: none;
			margin-bottom: 0;
			padding-left: 0;
			text-transform: uppercase;
		}

			#nav ul.links li {
				display: block;
				padding-left: 0;
			}

				#nav ul.links li a {
					-moz-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
					-webkit-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
					-ms-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
					transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
					display: block;
					font-size: 0.8rem;
					outline: none;
					padding: 0 2rem;
				}

					#nav ul.links li a:hover {
						color: inherit !important;
						background-color: rgba(255, 255, 255, 0.1);
					}

				#nav ul.links li.active {
					background-color: #ffffff;
				}

					#nav ul.links li.active a {
						color: #002b55;
					}

						#nav ul.links li.active a:hover {
							color: #18bfef !important;
						}

		#nav ul.icons {
			-moz-flex-grow: 0;
			-webkit-flex-grow: 0;
			-ms-flex-grow: 0;
			flex-grow: 0;
			-moz-flex-shrink: 0;
			-webkit-flex-shrink: 0;
			-ms-flex-shrink: 0;
			flex-shrink: 0;
			margin-bottom: 0;
		}

		@media screen and (max-width: 980px) {

			#nav {
				display: none;
			}

		}

/* Main */

	#main {
		background-color: #ffffff;
		position: relative;
		margin: 0 auto;
		width: calc(100% - 4rem);
		max-width: 72rem;
		z-index: 2;
	}

		#main > * {
			padding: 4rem 4rem 2rem 4rem ;
			border-top: solid 2px #eeeeee;
			margin: 0;
		}

			#main > *:first-child {
				border-top: 0;
			}

		#main > footer {
			text-align: center;
		}

		#main > .post {
			padding: 8rem 8rem 6rem 8rem ;
		}

			#main > .post header.major > .date {
				margin-top: -2rem;
			}

			#main > .post header.major > h1, #main > .post header.major h2 {
				font-size: 4rem;
				line-height: 1.1;
				margin: 0 0 2rem 0;
			}

			#main > .post.featured {
				text-align: center;
			}

			@media screen and (max-width: 1280px) {

				#main > .post {
					padding: 6rem 4rem 4rem 4rem ;
				}

			}

			@media screen and (max-width: 736px) {

				#main > .post {
					padding: 4rem 2rem 2rem 2rem ;
				}

					#main > .post header.major > .date {
						margin-top: -1rem;
						margin-bottom: 2rem;
					}

					#main > .post header.major > h1, #main > .post header.major h2 {
						font-size: 2.5rem;
						line-height: 1.2;
						margin: 0 0 1.5rem 0;
					}

			}

		#main > .posts {
			display: -moz-flex;
			display: -webkit-flex;
			display: -ms-flex;
			display: flex;
			-moz-flex-wrap: wrap;
			-webkit-flex-wrap: wrap;
			-ms-flex-wrap: wrap;
			flex-wrap: wrap;
			-moz-align-items: stretch;
			-webkit-align-items: stretch;
			-ms-align-items: stretch;
			align-items: stretch;
			text-align: center;
			width: 100%;
			padding: 0;
		}

			#main > .posts > * {
				-moz-flex-shrink: 1;
				-webkit-flex-shrink: 1;
				-ms-flex-shrink: 1;
				flex-shrink: 1;
				-moz-flex-grow: 0;
				-webkit-flex-grow: 0;
				-ms-flex-grow: 0;
				flex-grow: 0;
			}

			#main > .posts > * {
				width: 50%;
			}

			#main > .posts > * {
				padding: 4rem;
				width: 50%;
			}

			#main > .posts > article {
				border-color: #eeeeee;
				border-left-width: 2px;
				border-style: solid;
				border-top-width: 2px;
				text-align: center;
			}

				#main > .posts > article > :last-child {
					margin-bottom: 0;
				}

				#main > .posts > article:nth-child(2n - 1) {
					border-left-width: 0;
				}

				#main > .posts > article:nth-child(-n + 2) {
					border-top-width: 0;
				}

			@media screen and (max-width: 980px) {

				#main > .posts > * {
					width: 50%;
				}

				#main > .posts > * {
					padding: 2.5rem;
					width: 50%;
				}

			}

			@media screen and (max-width: 736px) {

				#main > .posts > * {
					width: 100%;
				}

				#main > .posts > * {
					padding: 2rem;
					width: 100%;
				}

				#main > .posts > article:nth-child(2n - 1) {
					border-left-width: 2px;
				}

				#main > .posts > article:nth-child(-n + 2) {
					border-top-width: 2px;
				}

				#main > .posts > article:nth-child(n) {
					border-left-width: 0;
				}

				#main > .posts > article:nth-child(-n + 1) {
					border-top-width: 0;
				}

				#main > .posts > article .image {
					max-width: 25rem;
					margin-left: auto;
					margin-right: auto;
				}

			}

		@media screen and (max-width: 736px) {

			#main > * {
				padding: 2rem 2rem 0.1rem 2rem ;
			}

		}

		@media screen and (max-width: 480px) {

			#main {
				width: 100%;
			}

		}

/* Footer */

	#footer {
		color: #717981;
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		background-color: #f5f5f5;
		color: #909498;
		cursor: default;
		position: relative;
		margin: 0 auto;
		width: calc(100% - 4rem);
		max-width: 72rem;
		z-index: 2;
	}

		#footer input, #footer select, #footer textarea {
			color: #717981;
		}

		#footer a {
			color: #717981;
			border-bottom-color: rgba(113, 121, 129, 0.5);
		}

			#footer a:hover {
				border-bottom-color: transparent;
				color: #18bfef !important;
			}

		#footer strong, #footer b {
			color: #717981;
		}

		#footer h1, #footer h2, #footer h3, #footer h4, #footer h5, #footer h6 {
			color: #717981;
		}

		#footer blockquote {
			border-left-color: #e2e2e2;
		}

		#footer code {
			background: rgba(220, 220, 220, 0.5);
			border-color: #e2e2e2;
		}

		#footer hr {
			border-bottom-color: #e2e2e2;
		}

		#footer .box {
			border-color: #e2e2e2;
		}

		#footer input[type="submit"],
		#footer input[type="reset"],
		#footer input[type="button"],
		#footer button,
		#footer .button {
			background-color: transparent;
			box-shadow: inset 0 0 0 2px #717981;
			color: #717981 !important;
		}

			#footer input[type="submit"]:hover,
			#footer input[type="reset"]:hover,
			#footer input[type="button"]:hover,
			#footer button:hover,
			#footer .button:hover {
				box-shadow: inset 0 0 0 2px #18bfef;
				color: #18bfef !important;
			}

			#footer input[type="submit"].special,
			#footer input[type="reset"].special,
			#footer input[type="button"].special,
			#footer button.special,
			#footer .button.special {
				background-color: #717981;
				box-shadow: none;
				color: #f5f5f5 !important;
			}

				#footer input[type="submit"].special:hover,
				#footer input[type="reset"].special:hover,
				#footer input[type="button"].special:hover,
				#footer button.special:hover,
				#footer .button.special:hover {
					background-color: #18bfef;
				}

		#footer label {
			color: #717981;
		}

		#footer input[type="text"],
		#footer input[type="password"],
		#footer input[type="email"],
		#footer select,
		#footer textarea {
			border-color: #e2e2e2;
		}

			#footer input[type="text"]:focus,
			#footer input[type="password"]:focus,
			#footer input[type="email"]:focus,
			#footer select:focus,
			#footer textarea:focus {
				border-color: #18bfef;
			}

		#footer select option {
			background-color: #f5f5f5;
			color: #717981;
		}

		#footer .select-wrapper:before {
			color: #e2e2e2;
		}

		#footer input[type="checkbox"] + label,
		#footer input[type="radio"] + label {
			color: #717981;
		}

			#footer input[type="checkbox"] + label:before,
			#footer input[type="radio"] + label:before {
				border-color: #e2e2e2;
			}

		#footer input[type="checkbox"]:checked + label:before,
		#footer input[type="radio"]:checked + label:before {
			background-color: #717981;
			border-color: #717981;
			color: #f5f5f5;
		}

		#footer input[type="checkbox"]:focus + label:before,
		#footer input[type="radio"]:focus + label:before {
			border-color: #18bfef;
		}

		#footer ::-webkit-input-placeholder {
			color: #b3b7bb !important;
		}

		#footer :-moz-placeholder {
			color: #b3b7bb !important;
		}

		#footer ::-moz-placeholder {
			color: #b3b7bb !important;
		}

		#footer :-ms-input-placeholder {
			color: #b3b7bb !important;
		}

		#footer .formerize-placeholder {
			color: #b3b7bb !important;
		}

		#footer ul.divided li {
			border-top-color: #e2e2e2;
		}

		#footer ul.icons li a.icon:hover:before {
			color: #18bfef;
		}

		#footer ul.icons.alt li .icon:before {
			box-shadow: inset 0 0 0 2px #e2e2e2;
		}

		#footer ul.icons.alt li a.icon:hover:before {
			box-shadow: inset 0 0 0 2px #18bfef;
		}

		#footer header.major .date:before, #footer header.major .date:after {
			border-top-color: #e2e2e2;
		}

		#footer table tbody tr {
			border-color: #e2e2e2;
		}

			#footer table tbody tr:nth-child(2n + 1) {
				background-color: rgba(220, 220, 220, 0.5);
			}

		#footer table th {
			color: #717981;
		}

		#footer table thead {
			border-bottom-color: #e2e2e2;
		}

		#footer table tfoot {
			border-top-color: #e2e2e2;
		}

		#footer table.alt tbody tr td {
			border-color: #e2e2e2;
		}

		#footer .pagination a, #footer .pagination span {
			border-color: #e2e2e2;
		}

		#footer .pagination a {
			color: #717981 !important;
		}

			#footer .pagination a:hover {
				color: #18bfef !important;
				border-color: #18bfef;
				z-index: 1;
			}

				#footer .pagination a:hover + a, #footer .pagination a:hover + span {
					border-left-color: #18bfef;
				}

			#footer .pagination a.active {
				background-color: #e2e2e2;
			}

		#footer .pagination span {
			color: #e2e2e2;
		}

		#footer > section {
			-moz-flex-basis: 50%;
			-webkit-flex-basis: 50%;
			-ms-flex-basis: 50%;
			flex-basis: 50%;
			-moz-flex-grow: 1;
			-webkit-flex-grow: 1;
			-ms-flex-grow: 1;
			flex-grow: 1;
			-moz-flex-shrink: 1;
			-webkit-flex-shrink: 1;
			-ms-flex-shrink: 1;
			flex-shrink: 1;
			padding: 4rem 4rem 2rem 4rem ;
			border-left: solid 2px #e2e2e2;
		}

			#footer > section:first-child {
				border-left: 0;
			}

			#footer > section.split {
				display: -moz-flex;
				display: -webkit-flex;
				display: -ms-flex;
				display: flex;
				-moz-flex-direction: column;
				-webkit-flex-direction: column;
				-ms-flex-direction: column;
				flex-direction: column;
				padding: 0;
			}

				#footer > section.split > section {
					padding: 3rem 4rem 1rem 4rem ;
					border-top: solid 2px #e2e2e2;
				}

					#footer > section.split > section:first-child {
						padding: 5rem 4rem 1rem 4rem ;
						border-top: 0;
					}

					#footer > section.split > section:last-child {
						padding: 3rem 4rem 3rem 4rem ;
					}

				#footer > section.split.contact > section {
					display: -moz-flex;
					display: -webkit-flex;
					display: -ms-flex;
					display: flex;
					-moz-align-items: center;
					-webkit-align-items: center;
					-ms-align-items: center;
					align-items: center;
					padding: 3.15rem 4rem;
				}

					#footer > section.split.contact > section > * {
						margin-bottom: 0;
					}

					#footer > section.split.contact > section > :first-child {
						-moz-flex-shrink: 0;
						-webkit-flex-shrink: 0;
						-ms-flex-shrink: 0;
						flex-shrink: 0;
						-moz-flex-grow: 0;
						-webkit-flex-grow: 0;
						-ms-flex-grow: 0;
						flex-grow: 0;
						width: 6rem;
					}

					#footer > section.split.contact > section > :last-child {
						-moz-flex-shrink: 1;
						-webkit-flex-shrink: 1;
						-ms-flex-shrink: 1;
						flex-shrink: 1;
						-moz-flex-grow: 1;
						-webkit-flex-grow: 1;
						-ms-flex-grow: 1;
						flex-grow: 1;
					}

					#footer > section.split.contact > section:first-child {
						padding: 4rem 4rem 3rem 4rem;
					}

					#footer > section.split.contact > section:last-child {
						padding: 3rem 4rem 4rem 4rem;
					}

					#footer > section.split.contact > section.alt {
						-moz-align-items: -moz-flex-start;
						-webkit-align-items: -webkit-flex-start;
						-ms-align-items: -ms-flex-start;
						align-items: flex-start;
					}

						#footer > section.split.contact > section.alt > :last-child {
							margin-top: -0.325rem;
						}

		#footer form label,
		#footer h3,
		#footer p {
			font-size: 0.8rem;
		}

		@media screen and (max-width: 980px) {

			#footer {
				display: block;
			}

				#footer > section {
					border-top: solid 2px #e2e2e2;
				}

					#footer > section:first-child {
						border-top: 0;
					}

					#footer > section.split > section {
						padding: 4rem 4rem 2rem 4rem ;
					}

						#footer > section.split > section:first-child {
							padding: 4rem 4rem 2rem 4rem ;
						}

						#footer > section.split > section:last-child {
							padding: 4rem 4rem 2rem 4rem ;
						}

					#footer > section.split.contact > section {
						padding: 4rem;
					}

						#footer > section.split.contact > section:first-child {
							padding: 4rem;
						}

						#footer > section.split.contact > section:last-child {
							padding: 4rem;
						}

				#footer form label,
				#footer h3,
				#footer p {
					font-size: 0.9rem;
				}

		}

		@media screen and (max-width: 736px) {

			#footer > section {
				padding: 2rem 2rem 0.1rem 2rem ;
			}

				#footer > section.split > section {
					padding: 2rem 2rem 0.1rem 2rem ;
				}

					#footer > section.split > section:first-child {
						padding: 2rem 2rem 0.1rem 2rem ;
					}

					#footer > section.split > section:last-child {
						padding: 2rem 2rem 0.1rem 2rem ;
					}

				#footer > section.split.contact > section {
					padding: 2rem;
				}

					#footer > section.split.contact > section:first-child {
						padding: 2rem;
					}

					#footer > section.split.contact > section:last-child {
						padding: 2rem;
					}

		}

		@media screen and (max-width: 480px) {

			#footer {
				width: 100%;
			}

		}

	#copyright {
		color: #ffffff;
		position: relative;
		color: rgba(255, 255, 255, 0.25);
		cursor: default;
		font-family: "Source Sans Pro", Helvetica, sans-serif;
		font-size: 0.8rem;
		font-weight: 900;
		letter-spacing: 0.075em;
		line-height: 1.5;
		text-align: center;
		text-transform: uppercase;
		margin: 4rem auto 8rem auto;
		width: calc(100% - 4rem);
		max-width: 72rem;
		z-index: 2;
	}

		#copyright input, #copyright select, #copyright textarea {
			color: #ffffff;
		}

		#copyright a {
			color: #ffffff;
			border-bottom-color: rgba(255, 255, 255, 0.5);
		}

			#copyright a:hover {
				border-bottom-color: transparent;
				color: #18bfef !important;
			}

		#copyright strong, #copyright b {
			color: #ffffff;
		}

		#copyright h1, #copyright h2, #copyright h3, #copyright h4, #copyright h5, #copyright h6 {
			color: #ffffff;
		}

		#copyright blockquote {
			border-left-color: #ffffff;
		}

		#copyright code {
			background: rgba(255, 255, 255, 0.075);
			border-color: #ffffff;
		}

		#copyright hr {
			border-bottom-color: #ffffff;
		}

		#copyright a {
			color: inherit;
			border-bottom-color: inherit;
		}

		#copyright ul {
			list-style: none;
			margin: 0;
			padding-left: 0;
		}

			#copyright ul li {
				border-left: solid 2px;
				display: inline-block;
				line-height: 1;
				margin-left: 1rem;
				padding-left: 1rem;
			}

				#copyright ul li:first-child {
					border-left: 0;
					margin-left: 0;
					padding-left: 0;
				}

		@media screen and (max-width: 1280px) {

			#copyright {
				margin: 4rem auto;
			}

		}

		@media screen and (max-width: 480px) {

			#copyright ul li {
				border-left: 0;
				margin: 1rem 0 0 0;
				padding-left: 0;
				display: block;
			}

				#copyright ul li:first-child {
					margin-top: 0;
				}

		}

/* Nav Panel */

	#navPanelToggle {
		text-decoration: none;
		-moz-transition: color 0.2s ease-in-out, background-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
		-webkit-transition: color 0.2s ease-in-out, background-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
		-ms-transition: color 0.2s ease-in-out, background-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
		transition: color 0.2s ease-in-out, background-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
		display: none;
		position: fixed;
		top: 0.75rem;
		right: 0.75rem;
		border: 0;
		color: #ffffff;
		font-family: "Source Sans Pro", Helvetica, sans-serif;
		font-size: 0.9rem;
		font-weight: 900;
		letter-spacing: 0.075em;
		padding: 0.375rem 1.25rem;
		text-transform: uppercase;
		z-index: 10001;
	}

		#navPanelToggle:before {
			-moz-osx-font-smoothing: grayscale;
			-webkit-font-smoothing: antialiased;
			font-family: FontAwesome;
			font-style: normal;
			font-weight: normal;
			text-transform: none !important;
		}

		#navPanelToggle:before {
			content: '\f0c9';
			margin-right: 0.5rem;
		}

		#navPanelToggle.alt {
			background-color: rgba(255, 255, 255, 0.875);
			box-shadow: 0 0.125rem 0.75rem 0 rgba(30, 37, 45, 0.25);
			color: #212931;
		}

			#navPanelToggle.alt:hover {
				background-color: #ffffff;
			}

		@media screen and (max-width: 980px) {

			#navPanelToggle {
				display: block;
			}

		}

		@media screen and (max-width: 736px) {

			#navPanelToggle {
				font-size: 0.8rem;
				padding: 0.25rem 1rem;
			}

		}

	#navPanel {
		-moz-transform: translateX(20rem);
		-webkit-transform: translateX(20rem);
		-ms-transform: translateX(20rem);
		transform: translateX(20rem);
		-moz-transition: -moz-transform 0.5s ease, box-shadow 0.5s ease, visibility 0.5s;
		-webkit-transition: -webkit-transform 0.5s ease, box-shadow 0.5s ease, visibility 0.5s;
		-ms-transition: -ms-transform 0.5s ease, box-shadow 0.5s ease, visibility 0.5s;
		transition: transform 0.5s ease, box-shadow 0.5s ease, visibility 0.5s;
		display: none;
		-webkit-overflow-scrolling: touch;
		background: #ffffff;
		box-shadow: none;
		color: #212931;
		height: 100%;
		max-width: 80%;
		overflow-y: auto;
		padding: 3rem 2rem;
		position: fixed;
		right: 0;
		top: 0;
		visibility: hidden;
		width: 20rem;
		z-index: 10002;
	}

		#navPanel .links {
			list-style: none;
			padding-left: 0;
		}

			#navPanel .links li {
				border-top: solid 2px #eeeeee;
			}

				#navPanel .links li a {
					border-bottom: 0;
					display: block;
					font-family: "Source Sans Pro", Helvetica, sans-serif;
					font-size: 0.9rem;
					font-size: 0.9rem;
					font-weight: 900;
					letter-spacing: 0.075em;
					padding: 0.75rem 0;
					text-transform: uppercase;
				}

				#navPanel .links li:first-child {
					border-top: 0;
				}

		#navPanel .close {
			text-decoration: none;
			-moz-transition: color 0.2s ease-in-out;
			-webkit-transition: color 0.2s ease-in-out;
			-ms-transition: color 0.2s ease-in-out;
			transition: color 0.2s ease-in-out;
			-webkit-tap-highlight-color: transparent;
			border: 0;
			color: #909498;
			cursor: pointer;
			display: block;
			height: 3.25rem;
			line-height: 3.25rem;
			padding-right: 1.25rem;
			position: absolute;
			right: 0;
			text-align: right;
			top: 0;
			vertical-align: middle;
			width: 7rem;
		}

			#navPanel .close:before {
				-moz-osx-font-smoothing: grayscale;
				-webkit-font-smoothing: antialiased;
				font-family: FontAwesome;
				font-style: normal;
				font-weight: normal;
				text-transform: none !important;
			}

			#navPanel .close:before {
				content: '\f00d';
				font-size: 1.25rem;
			}

			#navPanel .close:hover {
				color: #212931;
			}

			@media screen and (max-width: 736px) {

				#navPanel .close {
					height: 4rem;
					line-height: 4rem;
				}

			}

		@media screen and (max-width: 980px) {

			#navPanel {
				display: block;
			}

		}

		@media screen and (max-width: 736px) {

			#navPanel {
				padding: 2.5rem 1.75rem;
			}

		}

	@media screen and (max-width: 980px) {

		body.is-navPanel-visible #wrapper {
			opacity: 0.5;
		}

		body.is-navPanel-visible #navPanel {
			-moz-transform: translateX(0);
			-webkit-transform: translateX(0);
			-ms-transform: translateX(0);
			transform: translateX(0);
			box-shadow: 0 0 1.5rem 0 rgba(0, 0, 0, 0.2);
			visibility: visible;
		}

	}
@import url(font-awesome.min.css);

/*
	Massively by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/

/* Wrapper */

	#wrapper {
		background-color: #212931;
		background-image: url("../../images/overlay.png"), linear-gradient(0deg, rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.1)), url("../../images/bg.jpg");
		background-size: auto,								auto,														100% auto;
		background-position: center,								center,														top center;
		background-repeat: repeat,								no-repeat,													no-repeat;
		background-attachment: fixed,								fixed,														fixed;
	}

		#wrapper.fade-in:before {
			display: none;
		}

/* Intro */

	body.is-loading #intro {
		opacity: 1;
	}

		body.is-loading #intro:not(.hidden) + #header + #nav {
			-moz-transform: none;
			-webkit-transform: none;
			-ms-transform: none;
			transform: none;
			opacity: 1;
		}
		/*!
 *  Font Awesome 4.6.3 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */@font-face{font-family:'FontAwesome';src:url('../fonts/fontawesome-webfont.eot?v=4.6.3');src:url('../fonts/fontawesome-webfont.eot?#iefix&v=4.6.3') format('embedded-opentype'),url('../fonts/fontawesome-webfont.woff2?v=4.6.3') format('woff2'),url('../fonts/fontawesome-webfont.woff?v=4.6.3') format('woff'),url('../fonts/fontawesome-webfont.ttf?v=4.6.3') format('truetype'),url('../fonts/fontawesome-webfont.svg?v=4.6.3#fontawesomeregular') format('svg');font-weight:normal;font-style:normal}.fa{display:inline-block;font:normal normal normal 14px/1 FontAwesome;font-size:inherit;text-rendering:auto;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.fa-lg{font-size:1.33333333em;line-height:.75em;vertical-align:-15%}.fa-2x{font-size:2em}.fa-3x{font-size:3em}.fa-4x{font-size:4em}.fa-5x{font-size:5em}.fa-fw{width:1.28571429em;text-align:center}.fa-ul{padding-left:0;margin-left:2.14285714em;list-style-type:none}.fa-ul>li{position:relative}.fa-li{position:absolute;left:-2.14285714em;width:2.14285714em;top:.14285714em;text-align:center}.fa-li.fa-lg{left:-1.85714286em}.fa-border{padding:.2em .25em .15em;border:solid .08em #eee;border-radius:.1em}.fa-pull-left{float:left}.fa-pull-right{float:right}.fa.fa-pull-left{margin-right:.3em}.fa.fa-pull-right{margin-left:.3em}.pull-right{float:right}.pull-left{float:left}.fa.pull-left{margin-right:.3em}.fa.pull-right{margin-left:.3em}.fa-spin{-webkit-animation:fa-spin 2s infinite linear;animation:fa-spin 2s infinite linear}.fa-pulse{-webkit-animation:fa-spin 1s infinite steps(8);animation:fa-spin 1s infinite steps(8)}@-webkit-keyframes fa-spin{0%{-webkit-transform:rotate(0deg);transform:rotate(0deg)}100%{-webkit-transform:rotate(359deg);transform:rotate(359deg)}}@keyframes fa-spin{0%{-webkit-transform:rotate(0deg);transform:rotate(0deg)}100%{-webkit-transform:rotate(359deg);transform:rotate(359deg)}}.fa-rotate-90{-ms-filter:"progid:DXImageTransform.Microsoft.BasicImage(rotation=1)";-webkit-transform:rotate(90deg);-ms-transform:rotate(90deg);transform:rotate(90deg)}.fa-rotate-180{-ms-filter:"progid:DXImageTransform.Microsoft.BasicImage(rotation=2)";-webkit-transform:rotate(180deg);-ms-transform:rotate(180deg);transform:rotate(180deg)}.fa-rotate-270{-ms-filter:"progid:DXImageTransform.Microsoft.BasicImage(rotation=3)";-webkit-transform:rotate(270deg);-ms-transform:rotate(270deg);transform:rotate(270deg)}.fa-flip-horizontal{-ms-filter:"progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1)";-webkit-transform:scale(-1, 1);-ms-transform:scale(-1, 1);transform:scale(-1, 1)}.fa-flip-vertical{-ms-filter:"progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";-webkit-transform:scale(1, -1);-ms-transform:scale(1, -1);transform:scale(1, -1)}:root .fa-rotate-90,:root .fa-rotate-180,:root .fa-rotate-270,:root .fa-flip-horizontal,:root .fa-flip-vertical{filter:none}.fa-stack{position:relative;display:inline-block;width:2em;height:2em;line-height:2em;vertical-align:middle}.fa-stack-1x,.fa-stack-2x{position:absolute;left:0;width:100%;text-align:center}.fa-stack-1x{line-height:inherit}.fa-stack-2x{font-size:2em}.fa-inverse{color:#fff}.fa-glass:before{content:"\f000"}.fa-music:before{content:"\f001"}.fa-search:before{content:"\f002"}.fa-envelope-o:before{content:"\f003"}.fa-heart:before{content:"\f004"}.fa-star:before{content:"\f005"}.fa-star-o:before{content:"\f006"}.fa-user:before{content:"\f007"}.fa-film:before{content:"\f008"}.fa-th-large:before{content:"\f009"}.fa-th:before{content:"\f00a"}.fa-th-list:before{content:"\f00b"}.fa-check:before{content:"\f00c"}.fa-remove:before,.fa-close:before,.fa-times:before{content:"\f00d"}.fa-search-plus:before{content:"\f00e"}.fa-search-minus:before{content:"\f010"}.fa-power-off:before{content:"\f011"}.fa-signal:before{content:"\f012"}.fa-gear:before,.fa-cog:before{content:"\f013"}.fa-trash-o:before{content:"\f014"}.fa-home:before{content:"\f015"}.fa-file-o:before{content:"\f016"}.fa-clock-o:before{content:"\f017"}.fa-road:before{content:"\f018"}.fa-download:before{content:"\f019"}.fa-arrow-circle-o-down:before{content:"\f01a"}.fa-arrow-circle-o-up:before{content:"\f01b"}.fa-inbox:before{content:"\f01c"}.fa-play-circle-o:before{content:"\f01d"}.fa-rotate-right:before,.fa-repeat:before{content:"\f01e"}.fa-refresh:before{content:"\f021"}.fa-list-alt:before{content:"\f022"}.fa-lock:before{content:"\f023"}.fa-flag:before{content:"\f024"}.fa-headphones:before{content:"\f025"}.fa-volume-off:before{content:"\f026"}.fa-volume-down:before{content:"\f027"}.fa-volume-up:before{content:"\f028"}.fa-qrcode:before{content:"\f029"}.fa-barcode:before{content:"\f02a"}.fa-tag:before{content:"\f02b"}.fa-tags:before{content:"\f02c"}.fa-book:before{content:"\f02d"}.fa-bookmark:before{content:"\f02e"}.fa-print:before{content:"\f02f"}.fa-camera:before{content:"\f030"}.fa-font:before{content:"\f031"}.fa-bold:before{content:"\f032"}.fa-italic:before{content:"\f033"}.fa-text-height:before{content:"\f034"}.fa-text-width:before{content:"\f035"}.fa-align-left:before{content:"\f036"}.fa-align-center:before{content:"\f037"}.fa-align-right:before{content:"\f038"}.fa-align-justify:before{content:"\f039"}.fa-list:before{content:"\f03a"}.fa-dedent:before,.fa-outdent:before{content:"\f03b"}.fa-indent:before{content:"\f03c"}.fa-video-camera:before{content:"\f03d"}.fa-photo:before,.fa-image:before,.fa-picture-o:before{content:"\f03e"}.fa-pencil:before{content:"\f040"}.fa-map-marker:before{content:"\f041"}.fa-adjust:before{content:"\f042"}.fa-tint:before{content:"\f043"}.fa-edit:before,.fa-pencil-square-o:before{content:"\f044"}.fa-share-square-o:before{content:"\f045"}.fa-check-square-o:before{content:"\f046"}.fa-arrows:before{content:"\f047"}.fa-step-backward:before{content:"\f048"}.fa-fast-backward:before{content:"\f049"}.fa-backward:before{content:"\f04a"}.fa-play:before{content:"\f04b"}.fa-pause:before{content:"\f04c"}.fa-stop:before{content:"\f04d"}.fa-forward:before{content:"\f04e"}.fa-fast-forward:before{content:"\f050"}.fa-step-forward:before{content:"\f051"}.fa-eject:before{content:"\f052"}.fa-chevron-left:before{content:"\f053"}.fa-chevron-right:before{content:"\f054"}.fa-plus-circle:before{content:"\f055"}.fa-minus-circle:before{content:"\f056"}.fa-times-circle:before{content:"\f057"}.fa-check-circle:before{content:"\f058"}.fa-question-circle:before{content:"\f059"}.fa-info-circle:before{content:"\f05a"}.fa-crosshairs:before{content:"\f05b"}.fa-times-circle-o:before{content:"\f05c"}.fa-check-circle-o:before{content:"\f05d"}.fa-ban:before{content:"\f05e"}.fa-arrow-left:before{content:"\f060"}.fa-arrow-right:before{content:"\f061"}.fa-arrow-up:before{content:"\f062"}.fa-arrow-down:before{content:"\f063"}.fa-mail-forward:before,.fa-share:before{content:"\f064"}.fa-expand:before{content:"\f065"}.fa-compress:before{content:"\f066"}.fa-plus:before{content:"\f067"}.fa-minus:before{content:"\f068"}.fa-asterisk:before{content:"\f069"}.fa-exclamation-circle:before{content:"\f06a"}.fa-gift:before{content:"\f06b"}.fa-leaf:before{content:"\f06c"}.fa-fire:before{content:"\f06d"}.fa-eye:before{content:"\f06e"}.fa-eye-slash:before{content:"\f070"}.fa-warning:before,.fa-exclamation-triangle:before{content:"\f071"}.fa-plane:before{content:"\f072"}.fa-calendar:before{content:"\f073"}.fa-random:before{content:"\f074"}.fa-comment:before{content:"\f075"}.fa-magnet:before{content:"\f076"}.fa-chevron-up:before{content:"\f077"}.fa-chevron-down:before{content:"\f078"}.fa-retweet:before{content:"\f079"}.fa-shopping-cart:before{content:"\f07a"}.fa-folder:before{content:"\f07b"}.fa-folder-open:before{content:"\f07c"}.fa-arrows-v:before{content:"\f07d"}.fa-arrows-h:before{content:"\f07e"}.fa-bar-chart-o:before,.fa-bar-chart:before{content:"\f080"}.fa-twitter-square:before{content:"\f081"}.fa-facebook-square:before{content:"\f082"}.fa-camera-retro:before{content:"\f083"}.fa-key:before{content:"\f084"}.fa-gears:before,.fa-cogs:before{content:"\f085"}.fa-comments:before{content:"\f086"}.fa-thumbs-o-up:before{content:"\f087"}.fa-thumbs-o-down:before{content:"\f088"}.fa-star-half:before{content:"\f089"}.fa-heart-o:before{content:"\f08a"}.fa-sign-out:before{content:"\f08b"}.fa-linkedin-square:before{content:"\f08c"}.fa-thumb-tack:before{content:"\f08d"}.fa-external-link:before{content:"\f08e"}.fa-sign-in:before{content:"\f090"}.fa-trophy:before{content:"\f091"}.fa-github-square:before{content:"\f092"}.fa-upload:before{content:"\f093"}.fa-lemon-o:before{content:"\f094"}.fa-phone:before{content:"\f095"}.fa-square-o:before{content:"\f096"}.fa-bookmark-o:before{content:"\f097"}.fa-phone-square:before{content:"\f098"}.fa-twitter:before{content:"\f099"}.fa-facebook-f:before,.fa-facebook:before{content:"\f09a"}.fa-github:before{content:"\f09b"}.fa-unlock:before{content:"\f09c"}.fa-credit-card:before{content:"\f09d"}.fa-feed:before,.fa-rss:before{content:"\f09e"}.fa-hdd-o:before{content:"\f0a0"}.fa-bullhorn:before{content:"\f0a1"}.fa-bell:before{content:"\f0f3"}.fa-certificate:before{content:"\f0a3"}.fa-hand-o-right:before{content:"\f0a4"}.fa-hand-o-left:before{content:"\f0a5"}.fa-hand-o-up:before{content:"\f0a6"}.fa-hand-o-down:before{content:"\f0a7"}.fa-arrow-circle-left:before{content:"\f0a8"}.fa-arrow-circle-right:before{content:"\f0a9"}.fa-arrow-circle-up:before{content:"\f0aa"}.fa-arrow-circle-down:before{content:"\f0ab"}.fa-globe:before{content:"\f0ac"}.fa-wrench:before{content:"\f0ad"}.fa-tasks:before{content:"\f0ae"}.fa-filter:before{content:"\f0b0"}.fa-briefcase:before{content:"\f0b1"}.fa-arrows-alt:before{content:"\f0b2"}.fa-group:before,.fa-users:before{content:"\f0c0"}.fa-chain:before,.fa-link:before{content:"\f0c1"}.fa-cloud:before{content:"\f0c2"}.fa-flask:before{content:"\f0c3"}.fa-cut:before,.fa-scissors:before{content:"\f0c4"}.fa-copy:before,.fa-files-o:before{content:"\f0c5"}.fa-paperclip:before{content:"\f0c6"}.fa-save:before,.fa-floppy-o:before{content:"\f0c7"}.fa-square:before{content:"\f0c8"}.fa-navicon:before,.fa-reorder:before,.fa-bars:before{content:"\f0c9"}.fa-list-ul:before{content:"\f0ca"}.fa-list-ol:before{content:"\f0cb"}.fa-strikethrough:before{content:"\f0cc"}.fa-underline:before{content:"\f0cd"}.fa-table:before{content:"\f0ce"}.fa-magic:before{content:"\f0d0"}.fa-truck:before{content:"\f0d1"}.fa-pinterest:before{content:"\f0d2"}.fa-pinterest-square:before{content:"\f0d3"}.fa-google-plus-square:before{content:"\f0d4"}.fa-google-plus:before{content:"\f0d5"}.fa-money:before{content:"\f0d6"}.fa-caret-down:before{content:"\f0d7"}.fa-caret-up:before{content:"\f0d8"}.fa-caret-left:before{content:"\f0d9"}.fa-caret-right:before{content:"\f0da"}.fa-columns:before{content:"\f0db"}.fa-unsorted:before,.fa-sort:before{content:"\f0dc"}.fa-sort-down:before,.fa-sort-desc:before{content:"\f0dd"}.fa-sort-up:before,.fa-sort-asc:before{content:"\f0de"}.fa-envelope:before{content:"\f0e0"}.fa-linkedin:before{content:"\f0e1"}.fa-rotate-left:before,.fa-undo:before{content:"\f0e2"}.fa-legal:before,.fa-gavel:before{content:"\f0e3"}.fa-dashboard:before,.fa-tachometer:before{content:"\f0e4"}.fa-comment-o:before{content:"\f0e5"}.fa-comments-o:before{content:"\f0e6"}.fa-flash:before,.fa-bolt:before{content:"\f0e7"}.fa-sitemap:before{content:"\f0e8"}.fa-umbrella:before{content:"\f0e9"}.fa-paste:before,.fa-clipboard:before{content:"\f0ea"}.fa-lightbulb-o:before{content:"\f0eb"}.fa-exchange:before{content:"\f0ec"}.fa-cloud-download:before{content:"\f0ed"}.fa-cloud-upload:before{content:"\f0ee"}.fa-user-md:before{content:"\f0f0"}.fa-stethoscope:before{content:"\f0f1"}.fa-suitcase:before{content:"\f0f2"}.fa-bell-o:before{content:"\f0a2"}.fa-coffee:before{content:"\f0f4"}.fa-cutlery:before{content:"\f0f5"}.fa-file-text-o:before{content:"\f0f6"}.fa-building-o:before{content:"\f0f7"}.fa-hospital-o:before{content:"\f0f8"}.fa-ambulance:before{content:"\f0f9"}.fa-medkit:before{content:"\f0fa"}.fa-fighter-jet:before{content:"\f0fb"}.fa-beer:before{content:"\f0fc"}.fa-h-square:before{content:"\f0fd"}.fa-plus-square:before{content:"\f0fe"}.fa-angle-double-left:before{content:"\f100"}.fa-angle-double-right:before{content:"\f101"}.fa-angle-double-up:before{content:"\f102"}.fa-angle-double-down:before{content:"\f103"}.fa-angle-left:before{content:"\f104"}.fa-angle-right:before{content:"\f105"}.fa-angle-up:before{content:"\f106"}.fa-angle-down:before{content:"\f107"}.fa-desktop:before{content:"\f108"}.fa-laptop:before{content:"\f109"}.fa-tablet:before{content:"\f10a"}.fa-mobile-phone:before,.fa-mobile:before{content:"\f10b"}.fa-circle-o:before{content:"\f10c"}.fa-quote-left:before{content:"\f10d"}.fa-quote-right:before{content:"\f10e"}.fa-spinner:before{content:"\f110"}.fa-circle:before{content:"\f111"}.fa-mail-reply:before,.fa-reply:before{content:"\f112"}.fa-github-alt:before{content:"\f113"}.fa-folder-o:before{content:"\f114"}.fa-folder-open-o:before{content:"\f115"}.fa-smile-o:before{content:"\f118"}.fa-frown-o:before{content:"\f119"}.fa-meh-o:before{content:"\f11a"}.fa-gamepad:before{content:"\f11b"}.fa-keyboard-o:before{content:"\f11c"}.fa-flag-o:before{content:"\f11d"}.fa-flag-checkered:before{content:"\f11e"}.fa-terminal:before{content:"\f120"}.fa-code:before{content:"\f121"}.fa-mail-reply-all:before,.fa-reply-all:before{content:"\f122"}.fa-star-half-empty:before,.fa-star-half-full:before,.fa-star-half-o:before{content:"\f123"}.fa-location-arrow:before{content:"\f124"}.fa-crop:before{content:"\f125"}.fa-code-fork:before{content:"\f126"}.fa-unlink:before,.fa-chain-broken:before{content:"\f127"}.fa-question:before{content:"\f128"}.fa-info:before{content:"\f129"}.fa-exclamation:before{content:"\f12a"}.fa-superscript:before{content:"\f12b"}.fa-subscript:before{content:"\f12c"}.fa-eraser:before{content:"\f12d"}.fa-puzzle-piece:before{content:"\f12e"}.fa-microphone:before{content:"\f130"}.fa-microphone-slash:before{content:"\f131"}.fa-shield:before{content:"\f132"}.fa-calendar-o:before{content:"\f133"}.fa-fire-extinguisher:before{content:"\f134"}.fa-rocket:before{content:"\f135"}.fa-maxcdn:before{content:"\f136"}.fa-chevron-circle-left:before{content:"\f137"}.fa-chevron-circle-right:before{content:"\f138"}.fa-chevron-circle-up:before{content:"\f139"}.fa-chevron-circle-down:before{content:"\f13a"}.fa-html5:before{content:"\f13b"}.fa-css3:before{content:"\f13c"}.fa-anchor:before{content:"\f13d"}.fa-unlock-alt:before{content:"\f13e"}.fa-bullseye:before{content:"\f140"}.fa-ellipsis-h:before{content:"\f141"}.fa-ellipsis-v:before{content:"\f142"}.fa-rss-square:before{content:"\f143"}.fa-play-circle:before{content:"\f144"}.fa-ticket:before{content:"\f145"}.fa-minus-square:before{content:"\f146"}.fa-minus-square-o:before{content:"\f147"}.fa-level-up:before{content:"\f148"}.fa-level-down:before{content:"\f149"}.fa-check-square:before{content:"\f14a"}.fa-pencil-square:before{content:"\f14b"}.fa-external-link-square:before{content:"\f14c"}.fa-share-square:before{content:"\f14d"}.fa-compass:before{content:"\f14e"}.fa-toggle-down:before,.fa-caret-square-o-down:before{content:"\f150"}.fa-toggle-up:before,.fa-caret-square-o-up:before{content:"\f151"}.fa-toggle-right:before,.fa-caret-square-o-right:before{content:"\f152"}.fa-euro:before,.fa-eur:before{content:"\f153"}.fa-gbp:before{content:"\f154"}.fa-dollar:before,.fa-usd:before{content:"\f155"}.fa-rupee:before,.fa-inr:before{content:"\f156"}.fa-cny:before,.fa-rmb:before,.fa-yen:before,.fa-jpy:before{content:"\f157"}.fa-ruble:before,.fa-rouble:before,.fa-rub:before{content:"\f158"}.fa-won:before,.fa-krw:before{content:"\f159"}.fa-bitcoin:before,.fa-btc:before{content:"\f15a"}.fa-file:before{content:"\f15b"}.fa-file-text:before{content:"\f15c"}.fa-sort-alpha-asc:before{content:"\f15d"}.fa-sort-alpha-desc:before{content:"\f15e"}.fa-sort-amount-asc:before{content:"\f160"}.fa-sort-amount-desc:before{content:"\f161"}.fa-sort-numeric-asc:before{content:"\f162"}.fa-sort-numeric-desc:before{content:"\f163"}.fa-thumbs-up:before{content:"\f164"}.fa-thumbs-down:before{content:"\f165"}.fa-youtube-square:before{content:"\f166"}.fa-youtube:before{content:"\f167"}.fa-xing:before{content:"\f168"}.fa-xing-square:before{content:"\f169"}.fa-youtube-play:before{content:"\f16a"}.fa-dropbox:before{content:"\f16b"}.fa-stack-overflow:before{content:"\f16c"}.fa-instagram:before{content:"\f16d"}.fa-flickr:before{content:"\f16e"}.fa-adn:before{content:"\f170"}.fa-bitbucket:before{content:"\f171"}.fa-bitbucket-square:before{content:"\f172"}.fa-tumblr:before{content:"\f173"}.fa-tumblr-square:before{content:"\f174"}.fa-long-arrow-down:before{content:"\f175"}.fa-long-arrow-up:before{content:"\f176"}.fa-long-arrow-left:before{content:"\f177"}.fa-long-arrow-right:before{content:"\f178"}.fa-apple:before{content:"\f179"}.fa-windows:before{content:"\f17a"}.fa-android:before{content:"\f17b"}.fa-linux:before{content:"\f17c"}.fa-dribbble:before{content:"\f17d"}.fa-skype:before{content:"\f17e"}.fa-foursquare:before{content:"\f180"}.fa-trello:before{content:"\f181"}.fa-female:before{content:"\f182"}.fa-male:before{content:"\f183"}.fa-gittip:before,.fa-gratipay:before{content:"\f184"}.fa-sun-o:before{content:"\f185"}.fa-moon-o:before{content:"\f186"}.fa-archive:before{content:"\f187"}.fa-bug:before{content:"\f188"}.fa-vk:before{content:"\f189"}.fa-weibo:before{content:"\f18a"}.fa-renren:before{content:"\f18b"}.fa-pagelines:before{content:"\f18c"}.fa-stack-exchange:before{content:"\f18d"}.fa-arrow-circle-o-right:before{content:"\f18e"}.fa-arrow-circle-o-left:before{content:"\f190"}.fa-toggle-left:before,.fa-caret-square-o-left:before{content:"\f191"}.fa-dot-circle-o:before{content:"\f192"}.fa-wheelchair:before{content:"\f193"}.fa-vimeo-square:before{content:"\f194"}.fa-turkish-lira:before,.fa-try:before{content:"\f195"}.fa-plus-square-o:before{content:"\f196"}.fa-space-shuttle:before{content:"\f197"}.fa-slack:before{content:"\f198"}.fa-envelope-square:before{content:"\f199"}.fa-wordpress:before{content:"\f19a"}.fa-openid:before{content:"\f19b"}.fa-institution:before,.fa-bank:before,.fa-university:before{content:"\f19c"}.fa-mortar-board:before,.fa-graduation-cap:before{content:"\f19d"}.fa-yahoo:before{content:"\f19e"}.fa-google:before{content:"\f1a0"}.fa-reddit:before{content:"\f1a1"}.fa-reddit-square:before{content:"\f1a2"}.fa-stumbleupon-circle:before{content:"\f1a3"}.fa-stumbleupon:before{content:"\f1a4"}.fa-delicious:before{content:"\f1a5"}.fa-digg:before{content:"\f1a6"}.fa-pied-piper-pp:before{content:"\f1a7"}.fa-pied-piper-alt:before{content:"\f1a8"}.fa-drupal:before{content:"\f1a9"}.fa-joomla:before{content:"\f1aa"}.fa-language:before{content:"\f1ab"}.fa-fax:before{content:"\f1ac"}.fa-building:before{content:"\f1ad"}.fa-child:before{content:"\f1ae"}.fa-paw:before{content:"\f1b0"}.fa-spoon:before{content:"\f1b1"}.fa-cube:before{content:"\f1b2"}.fa-cubes:before{content:"\f1b3"}.fa-behance:before{content:"\f1b4"}.fa-behance-square:before{content:"\f1b5"}.fa-steam:before{content:"\f1b6"}.fa-steam-square:before{content:"\f1b7"}.fa-recycle:before{content:"\f1b8"}.fa-automobile:before,.fa-car:before{content:"\f1b9"}.fa-cab:before,.fa-taxi:before{content:"\f1ba"}.fa-tree:before{content:"\f1bb"}.fa-spotify:before{content:"\f1bc"}.fa-deviantart:before{content:"\f1bd"}.fa-soundcloud:before{content:"\f1be"}.fa-database:before{content:"\f1c0"}.fa-file-pdf-o:before{content:"\f1c1"}.fa-file-word-o:before{content:"\f1c2"}.fa-file-excel-o:before{content:"\f1c3"}.fa-file-powerpoint-o:before{content:"\f1c4"}.fa-file-photo-o:before,.fa-file-picture-o:before,.fa-file-image-o:before{content:"\f1c5"}.fa-file-zip-o:before,.fa-file-archive-o:before{content:"\f1c6"}.fa-file-sound-o:before,.fa-file-audio-o:before{content:"\f1c7"}.fa-file-movie-o:before,.fa-file-video-o:before{content:"\f1c8"}.fa-file-code-o:before{content:"\f1c9"}.fa-vine:before{content:"\f1ca"}.fa-codepen:before{content:"\f1cb"}.fa-jsfiddle:before{content:"\f1cc"}.fa-life-bouy:before,.fa-life-buoy:before,.fa-life-saver:before,.fa-support:before,.fa-life-ring:before{content:"\f1cd"}.fa-circle-o-notch:before{content:"\f1ce"}.fa-ra:before,.fa-resistance:before,.fa-rebel:before{content:"\f1d0"}.fa-ge:before,.fa-empire:before{content:"\f1d1"}.fa-git-square:before{content:"\f1d2"}.fa-git:before{content:"\f1d3"}.fa-y-combinator-square:before,.fa-yc-square:before,.fa-hacker-news:before{content:"\f1d4"}.fa-tencent-weibo:before{content:"\f1d5"}.fa-qq:before{content:"\f1d6"}.fa-wechat:before,.fa-weixin:before{content:"\f1d7"}.fa-send:before,.fa-paper-plane:before{content:"\f1d8"}.fa-send-o:before,.fa-paper-plane-o:before{content:"\f1d9"}.fa-history:before{content:"\f1da"}.fa-circle-thin:before{content:"\f1db"}.fa-header:before{content:"\f1dc"}.fa-paragraph:before{content:"\f1dd"}.fa-sliders:before{content:"\f1de"}.fa-share-alt:before{content:"\f1e0"}.fa-share-alt-square:before{content:"\f1e1"}.fa-bomb:before{content:"\f1e2"}.fa-soccer-ball-o:before,.fa-futbol-o:before{content:"\f1e3"}.fa-tty:before{content:"\f1e4"}.fa-binoculars:before{content:"\f1e5"}.fa-plug:before{content:"\f1e6"}.fa-slideshare:before{content:"\f1e7"}.fa-twitch:before{content:"\f1e8"}.fa-yelp:before{content:"\f1e9"}.fa-newspaper-o:before{content:"\f1ea"}.fa-wifi:before{content:"\f1eb"}.fa-calculator:before{content:"\f1ec"}.fa-paypal:before{content:"\f1ed"}.fa-google-wallet:before{content:"\f1ee"}.fa-cc-visa:before{content:"\f1f0"}.fa-cc-mastercard:before{content:"\f1f1"}.fa-cc-discover:before{content:"\f1f2"}.fa-cc-amex:before{content:"\f1f3"}.fa-cc-paypal:before{content:"\f1f4"}.fa-cc-stripe:before{content:"\f1f5"}.fa-bell-slash:before{content:"\f1f6"}.fa-bell-slash-o:before{content:"\f1f7"}.fa-trash:before{content:"\f1f8"}.fa-copyright:before{content:"\f1f9"}.fa-at:before{content:"\f1fa"}.fa-eyedropper:before{content:"\f1fb"}.fa-paint-brush:before{content:"\f1fc"}.fa-birthday-cake:before{content:"\f1fd"}.fa-area-chart:before{content:"\f1fe"}.fa-pie-chart:before{content:"\f200"}.fa-line-chart:before{content:"\f201"}.fa-lastfm:before{content:"\f202"}.fa-lastfm-square:before{content:"\f203"}.fa-toggle-off:before{content:"\f204"}.fa-toggle-on:before{content:"\f205"}.fa-bicycle:before{content:"\f206"}.fa-bus:before{content:"\f207"}.fa-ioxhost:before{content:"\f208"}.fa-angellist:before{content:"\f209"}.fa-cc:before{content:"\f20a"}.fa-shekel:before,.fa-sheqel:before,.fa-ils:before{content:"\f20b"}.fa-meanpath:before{content:"\f20c"}.fa-buysellads:before{content:"\f20d"}.fa-connectdevelop:before{content:"\f20e"}.fa-dashcube:before{content:"\f210"}.fa-forumbee:before{content:"\f211"}.fa-leanpub:before{content:"\f212"}.fa-sellsy:before{content:"\f213"}.fa-shirtsinbulk:before{content:"\f214"}.fa-simplybuilt:before{content:"\f215"}.fa-skyatlas:before{content:"\f216"}.fa-cart-plus:before{content:"\f217"}.fa-cart-arrow-down:before{content:"\f218"}.fa-diamond:before{content:"\f219"}.fa-ship:before{content:"\f21a"}.fa-user-secret:before{content:"\f21b"}.fa-motorcycle:before{content:"\f21c"}.fa-street-view:before{content:"\f21d"}.fa-heartbeat:before{content:"\f21e"}.fa-venus:before{content:"\f221"}.fa-mars:before{content:"\f222"}.fa-mercury:before{content:"\f223"}.fa-intersex:before,.fa-transgender:before{content:"\f224"}.fa-transgender-alt:before{content:"\f225"}.fa-venus-double:before{content:"\f226"}.fa-mars-double:before{content:"\f227"}.fa-venus-mars:before{content:"\f228"}.fa-mars-stroke:before{content:"\f229"}.fa-mars-stroke-v:before{content:"\f22a"}.fa-mars-stroke-h:before{content:"\f22b"}.fa-neuter:before{content:"\f22c"}.fa-genderless:before{content:"\f22d"}.fa-facebook-official:before{content:"\f230"}.fa-pinterest-p:before{content:"\f231"}.fa-whatsapp:before{content:"\f232"}.fa-server:before{content:"\f233"}.fa-user-plus:before{content:"\f234"}.fa-user-times:before{content:"\f235"}.fa-hotel:before,.fa-bed:before{content:"\f236"}.fa-viacoin:before{content:"\f237"}.fa-train:before{content:"\f238"}.fa-subway:before{content:"\f239"}.fa-medium:before{content:"\f23a"}.fa-yc:before,.fa-y-combinator:before{content:"\f23b"}.fa-optin-monster:before{content:"\f23c"}.fa-opencart:before{content:"\f23d"}.fa-expeditedssl:before{content:"\f23e"}.fa-battery-4:before,.fa-battery-full:before{content:"\f240"}.fa-battery-3:before,.fa-battery-three-quarters:before{content:"\f241"}.fa-battery-2:before,.fa-battery-half:before{content:"\f242"}.fa-battery-1:before,.fa-battery-quarter:before{content:"\f243"}.fa-battery-0:before,.fa-battery-empty:before{content:"\f244"}.fa-mouse-pointer:before{content:"\f245"}.fa-i-cursor:before{content:"\f246"}.fa-object-group:before{content:"\f247"}.fa-object-ungroup:before{content:"\f248"}.fa-sticky-note:before{content:"\f249"}.fa-sticky-note-o:before{content:"\f24a"}.fa-cc-jcb:before{content:"\f24b"}.fa-cc-diners-club:before{content:"\f24c"}.fa-clone:before{content:"\f24d"}.fa-balance-scale:before{content:"\f24e"}.fa-hourglass-o:before{content:"\f250"}.fa-hourglass-1:before,.fa-hourglass-start:before{content:"\f251"}.fa-hourglass-2:before,.fa-hourglass-half:before{content:"\f252"}.fa-hourglass-3:before,.fa-hourglass-end:before{content:"\f253"}.fa-hourglass:before{content:"\f254"}.fa-hand-grab-o:before,.fa-hand-rock-o:before{content:"\f255"}.fa-hand-stop-o:before,.fa-hand-paper-o:before{content:"\f256"}.fa-hand-scissors-o:before{content:"\f257"}.fa-hand-lizard-o:before{content:"\f258"}.fa-hand-spock-o:before{content:"\f259"}.fa-hand-pointer-o:before{content:"\f25a"}.fa-hand-peace-o:before{content:"\f25b"}.fa-trademark:before{content:"\f25c"}.fa-registered:before{content:"\f25d"}.fa-creative-commons:before{content:"\f25e"}.fa-gg:before{content:"\f260"}.fa-gg-circle:before{content:"\f261"}.fa-tripadvisor:before{content:"\f262"}.fa-odnoklassniki:before{content:"\f263"}.fa-odnoklassniki-square:before{content:"\f264"}.fa-get-pocket:before{content:"\f265"}.fa-wikipedia-w:before{content:"\f266"}.fa-safari:before{content:"\f267"}.fa-chrome:before{content:"\f268"}.fa-firefox:before{content:"\f269"}.fa-opera:before{content:"\f26a"}.fa-internet-explorer:before{content:"\f26b"}.fa-tv:before,.fa-television:before{content:"\f26c"}.fa-contao:before{content:"\f26d"}.fa-500px:before{content:"\f26e"}.fa-amazon:before{content:"\f270"}.fa-calendar-plus-o:before{content:"\f271"}.fa-calendar-minus-o:before{content:"\f272"}.fa-calendar-times-o:before{content:"\f273"}.fa-calendar-check-o:before{content:"\f274"}.fa-industry:before{content:"\f275"}.fa-map-pin:before{content:"\f276"}.fa-map-signs:before{content:"\f277"}.fa-map-o:before{content:"\f278"}.fa-map:before{content:"\f279"}.fa-commenting:before{content:"\f27a"}.fa-commenting-o:before{content:"\f27b"}.fa-houzz:before{content:"\f27c"}.fa-vimeo:before{content:"\f27d"}.fa-black-tie:before{content:"\f27e"}.fa-fonticons:before{content:"\f280"}.fa-reddit-alien:before{content:"\f281"}.fa-edge:before{content:"\f282"}.fa-credit-card-alt:before{content:"\f283"}.fa-codiepie:before{content:"\f284"}.fa-modx:before{content:"\f285"}.fa-fort-awesome:before{content:"\f286"}.fa-usb:before{content:"\f287"}.fa-product-hunt:before{content:"\f288"}.fa-mixcloud:before{content:"\f289"}.fa-scribd:before{content:"\f28a"}.fa-pause-circle:before{content:"\f28b"}.fa-pause-circle-o:before{content:"\f28c"}.fa-stop-circle:before{content:"\f28d"}.fa-stop-circle-o:before{content:"\f28e"}.fa-shopping-bag:before{content:"\f290"}.fa-shopping-basket:before{content:"\f291"}.fa-hashtag:before{content:"\f292"}.fa-bluetooth:before{content:"\f293"}.fa-bluetooth-b:before{content:"\f294"}.fa-percent:before{content:"\f295"}.fa-gitlab:before{content:"\f296"}.fa-wpbeginner:before{content:"\f297"}.fa-wpforms:before{content:"\f298"}.fa-envira:before{content:"\f299"}.fa-universal-access:before{content:"\f29a"}.fa-wheelchair-alt:before{content:"\f29b"}.fa-question-circle-o:before{content:"\f29c"}.fa-blind:before{content:"\f29d"}.fa-audio-description:before{content:"\f29e"}.fa-volume-control-phone:before{content:"\f2a0"}.fa-braille:before{content:"\f2a1"}.fa-assistive-listening-systems:before{content:"\f2a2"}.fa-asl-interpreting:before,.fa-american-sign-language-interpreting:before{content:"\f2a3"}.fa-deafness:before,.fa-hard-of-hearing:before,.fa-deaf:before{content:"\f2a4"}.fa-glide:before{content:"\f2a5"}.fa-glide-g:before{content:"\f2a6"}.fa-signing:before,.fa-sign-language:before{content:"\f2a7"}.fa-low-vision:before{content:"\f2a8"}.fa-viadeo:before{content:"\f2a9"}.fa-viadeo-square:before{content:"\f2aa"}.fa-snapchat:before{content:"\f2ab"}.fa-snapchat-ghost:before{content:"\f2ac"}.fa-snapchat-square:before{content:"\f2ad"}.fa-pied-piper:before{content:"\f2ae"}.fa-first-order:before{content:"\f2b0"}.fa-yoast:before{content:"\f2b1"}.fa-themeisle:before{content:"\f2b2"}.fa-google-plus-circle:before,.fa-google-plus-official:before{content:"\f2b3"}.fa-fa:before,.fa-font-awesome:before{content:"\f2b4"}.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0, 0, 0, 0);border:0}.sr-only-focusable:active,.sr-only-focusable:focus{position:static;width:auto;height:auto;margin:0;overflow:visible;clip:auto}
