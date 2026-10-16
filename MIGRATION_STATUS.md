# Migration and SEO status - October 9, 2026
## Current verified state
Main site is published at https://winchlawfirm.com/ on Netlify project majestic-cajeta-b5cfbd (50259f63-1a06-4d44-80b1-36fe24a8e725), with source WINCHLAW/winchlawfirmwebsite main.
Production deploy 6ac79c58b81b99000808ed1a published October8 at13:36:39Z from commit e30abec732b01da371378ef5fa3c0988bbaa2286, including West Fork Creek / Project Omega page.
Git delivery demonstrated again: commit72f68e5150f3342490e95df478ac882874993b58 triggered deploy6ac79e5d05635e0007af1d14, ready and published October8 at13:45:13Z.
Earlier notes claiming the main site remains on Wix, no Netlify plugin exists, or Git connection is unestablished are superseded. Do not rebuild or re-import the site. Publishing does not complete all acceptance gates.

## October 9 executed SEO improvement - Project Omega discovery
Evidence selected the homepage as the highest-value linking surface: GSC September11-October8 reports6 clicks/60 impressions/10% CTR/average position3.1667 for the HTTPS www homepage; GA4 property555762522 reports59 homepage landing sessions,45 active users and33 engaged sessions. The newly published West Fork Creek / Project Omega page had no homepage link.
Executed: added a visible Project Omega card in the homepage "Find your path" section linking to /west-fork-creek. Commit bb5b4120d37f8aa78902149741d75b5d0e4f685c triggered production deploy6ac8f063731a5900082d5fcb.
Verified live October9: deploy ready/published13:47:25Z; homepage card resolves to https://winchlawfirm.com/west-fork-creek; destination H1, canonical https://winchlawfirm.com/west-fork-creek, GTM container, dedicated expropriation phone and consultation links load. This internal-link task is complete.
A second focused internal-link task completed October9: added a Project Omega card to /legal-resources, the site's Louisiana property-rights resource hub. Commit e28900b3479baffbfcaaf28d0ed20d189ce2aed6 triggered production deploy6ac8fda9e46b8000087c54a7, ready/published14:44:03Z. Verified live: the resource page exposes the card, canonical https://winchlawfirm.com/legal-resources, and the card resolves to /west-fork-creek.

## Today's executed repair - consultation capture
Before: live /book-online had Netlify form markup, but processing was disabled and get_forms returned[].
Executed: enabled Netlify Forms via authorized plugin; committed status change to trigger the connected build.
Verified: processing enabled; consultation form6ac79e68ad0ab40008f63ca1 registered at13:45:12Z, fields name/email/phone/topic/message/document/acknowledgment plus honeypot. Live HTML confirms Netlify processed the form. Dedicated expropriation phone504-377-2620 and general504-500-1899 remain distinct.
Synthetic test: POSTed a multipart consultation with a dummy PDF containing no client data, using the firm's own email. HTTP200, request01M4DW7YZBZH9K14GBKH0XX6ZA. Netlify last_submission_at changed to2026-10-08T13:46:31.986Z; verified submission_count remains0. Do not claim verified storage or upload retrieval. Possible spam filtering, not confirmed.
Outlook search from:formresponses@netlify.com received>=2026-10-08 returned no messages. This does not establish whether notifications are configured.
Exact remaining blocker: plugin exposes form metadata/count, not submission contents, spam classification, marking verified, or notification settings. Browser is signed out; this scheduled run cannot complete interactive authentication. Next action is inspect this single synthetic test in Forms > consultation > Spam/Verified submissions and verify its PDF and notification destination.
Concrete done condition: verified stored inquiry with retrievable dummy PDF, and receipt at the firm's configured inbox. Form detection is fixed; end-to-end delivery remains unfinished.

## Analytics evidence
Period September11-October8,2026; comparison August14-September10,2026.
GA4 requested property417150352 winchlawfirmgoogleanalytics: completed empty current and prior results, not proof of zero traffic.
Separately connected GA4 property555762522 Property1: homepage landing row59 sessions,45 active users,33 engaged sessions,55.93% engagement; /book-online1 session/0 engaged; /louisiana-landowner-bill-of-rights2 sessions/0 engaged; (not set)6 sessions. Source/medium report includes google/organic11 sessions,10 active users,10 engaged sessions; direct37 sessions,32 active users,10 engaged sessions. Event report returned133 page views,23 clicks,1 document_open and1 file_download; all returned key-event counts0 and no contact/consultation event row. Prior-period reads returned no rows; do not report percentage growth from an empty comparison.
GSC sc-domain:winchlawfirm.com recent period with provisional fresh data:
- HTTPS www homepage:6 clicks,60 impressions,10% CTR,average position3.1667.
- HTTPS Entergy homepage:0 clicks,13 impressions,0% CTR,position3.5385.
- HTTPS Babel homepage:0 clicks,2 impressions,0% CTR,position8.
- Historical HTTP Babel homepage:1 click,1 impression,position1; historical HTTP www homepage:0 clicks,2 impressions,position6.5.
Prior period returned no rows. Query report exposes3 clicks for 'the firm'; remaining exposed queries are small-volume Abbeville legal terms with no clicks. Omitted/anonymized queries prevent classifying all page-level clicks. No identifiable visitors inferred.

## Prioritized queue
1. Main consultation form: repair executed and detection verified today; delivery/upload/spam/notification gate remains unfinished. Carry this gate forward, not repeat enabling detection.
2. Specialty social metadata: Entergy canonical and og:url now correctly https://entergy.winchlawfirm.com/; live og:image and twitter:image remain assets/og-cover.png. Babel canonical correctly https://entergybabelwebre.winchlawfirm.com/; Open Graph/Twitter tags absent. Prepared older files must be rebased onto latest live source before publishing to preserve October7 intake and Tag Manager changes. Entergy deploy6ac6d565094257480cd322be includes submit-review function and is not Git-backed per commit metadata.
3. Specialty robots/sitemaps: inspect actual public routes before composing/publishing.
4. GA property/stream reconciliation and live contact-event verification; do not remove existing Tag Manager based merely on absence of literal G-ID in HTML.
Navigation: the firm reported complete October2; specialty links verified October7. Do not repeat installation.
Main migration launch gates still pending: desktop/mobile rendering, all preserved routes/assets, end-to-end inquiry and upload receipt, notifications, GA receipt and key events, www/apex routing and preserved DNS/email records. Git deployment now verified.

## Creative candidate queue - research only
BREC Baton Rouge Zoo bald-eagle adoption: primary pages https://brzoo.org/support/adopt-an-animal and https://brzoo.org/animals/bald-eagle checked October8. Bald eagle listed; Go Green25 dollars/year, renewable, emailed certificate/keeper report/high-resolution photo. New planning detail: zoo says processing takes3-4 weeks. Species page does not identify resident bird's name, sex, individual story or current exhibit status. Commercial photo permission and public firm-adoption wording remain unverified.
Audience: Louisiana conservation/community families and potential local referrers; connection is the firm's eagle-and-land identity and actual regional conservation support, not a claim of legal referrals or ranking gains.
Next small action: retain this unsent question for a later authorized inquiry: 'Before Winch Law Firm adopts the bald eagle, can you confirm the resident bird's name/story/current exhibit status and whether the package photo may appear on a commercial firm website with credit? Is any public wording approval required?'
No outreach, spending, adoption or marketing publication performed. An outbound zoo link is a reference from our site; an independently earned inbound link is the zoo's separate editorial decision; a paid sponsorship link needs rel=sponsored or appropriate nofollow qualification. No backlink/endorsement/exclusivity promised.
Fair/show-pig candidate advanced October9: LSU AgCenter confirms the2027 State 4-H/FFA Livestock Show for February13-20,2027 at Lamar Dixon Expo Center in Gonzales. Its official sponsorship page supports the Livestock Youth Development Fund; published2026 major levels began at$2,500, which is outside the current inexpensive-candidate target. A prior Acadia Parish buckle sponsorship was$150, but the published deadline was November3,2025 and is stale-not a current offer. Next bounded action: watch for a2027 parish-level buckle/market-hog award opportunity at or below$250 before any outreach or spending. Audience is Louisiana 4-H/FFA exhibitors, agricultural families and rural referrers; the connection is real youth agricultural support, not a promised SEO link or endorsement.

## Preserved source/content
Existing main text and both articles retained in migration/ and generated routes.
/louisiana-landowner-bill-of-rights, /legal-resources, /blog,
/post/received-utility-right-of-way-offer-letter-louisiana,
/post/should-i-sign-utility-servitude-agreement-louisiana,
/book-online, /privacy, /thank-you, /west-fork-creek.
Static eagle, no splash animation. Newsletter/member notifications not migrated as services. Article illustration full-resolution archival before Wix retirement remains unverified.


## October 11, 2026 - automated SEO and activity review (executed)
### Data sources and window
- GA4 connector discovery still shows two properties. The named property `winchlawfirmgoogleanalytics` (account `417150352`) returned an empty result for this request; that is an access/property-mapping issue, not evidence of zero traffic.
- The connected GA4 property `Property1` (account `555762522`) returned data for 2026-09-13 through 2026-10-10. No valid prior-period rows were returned, so no growth percentage is asserted.
- Search Console property `sc-domain:winchlawfirm.com` returned data for the same 28-day window.

### Activity evidence
- GA4 Property1: 88 sessions, 58 active users on the recorded landing-page rows; the homepage accounted for 78 sessions, 58 active users, and 46 engaged sessions (58.97% engagement).
- Source/medium: direct 50 sessions (36% engagement), Google organic 16 sessions (87.5% engagement), and one `direct_mail / qr` session with engagement.
- Recorded key events: `generate_lead` 5 (5 marked conversions), `document_open` 2 (1 marked conversion), `form_start` 5, `form_submit` 1. These events need destination/receipt verification before being treated as qualified inquiries.
- Search Console: site aggregate was 9 clicks, 93 impressions, 9.68% CTR, average position 4.12. The Entergy page had 17 impressions and 0 clicks at average position 3.88; the Louisiana utility-servitude article had 1 click from 5 impressions at average position 8.4.

### Live technical review
- `https://entergy.winchlawfirm.com/` returned HTTP 200. Canonical and `og:url` are correct, but `og:image` and `twitter:image` still use the relative value `assets/og-cover.png`.
- `https://entergybabelwebre.winchlawfirm.com/` returned HTTP 200 and a correct canonical, but no Open Graph or Twitter image/title/description tags were present in the live HTML.
- `https://businesslegal.winchlawfirm.com/` returned HTTP 200 and a correct canonical, but the live `og:image` is the literal placeholder `[OG_IMAGE_URL]`; this is now queued as a metadata defect.
- Main site returned HTTP 200 with canonical, `og:url`, and absolute social image URLs. Specialty robots.txt and sitemap.xml endpoints returned HTTP 200.

### Action state
- COMPLETE/VERIFIED: live measurement pass and evidence recorded above.
- PREPARED (not deployed): corrected Entergy absolute image URLs and Babel Open Graph/Twitter tags exist in local review files.
- BLOCKED: publishing those specialty metadata fixes. The connected Netlify tools expose project/deploy reads but no deploy/upload write operation, and the specialty sites are not represented by source files in `WINCHLAW/winchlawfirmwebsite`. No claim of deployment is made.
- NEXT QUEUE: publish the specialty metadata patch through a connected Git-backed source or the existing Netlify deploy workflow; then fetch live HTML again and verify canonical, `og:url`, and absolute social images. After that, verify the consultation/document form's actual receipt and notification path.

## October 12, 2026 - authorized phone assignments and placeholder audit
The user explicitly reassigned general/main and Business Legal inquiries to 504-377-2620, and Entergy, Babel-Webre and Project Omega/expropriation inquiries to 504-500-1899. This supersedes the prior reversed phone assignments above. Updated the main-site source footer, homepage Entergy contact, consultation contact text and Project Omega contact, with matching tel links. No legal substance, forms, routing, canonical metadata or indexing settings changed.
Validation before publication: Python build (UTF-8 mode on Windows), all 12 generated HTML documents passed the existing site checks, and JavaScript syntax check passed. Deployment/live verification must be checked against the resulting commit; this entry alone is not proof of publication.
Live audit: 33 public URLs checked, 30 successful. Main repository and inspected main/Babel pages contain no LSBA filing placeholder. Entergy home, its netlify.app alias and current immutable deploy permalink still expose the placeholder. Prepared a narrow removal retaining attorney-advertising and responsible-lawyer disclosures. Business Legal also has unfinished image, scope note and article placeholders; cleanup and phone patches are prepared separately, not deployed.
Specialty publication is blocked in this execution environment: connector tools lack deploy/upload operations, no local Netlify CLI login/source bundle was found, and supported browser initialization failed. Specialty sites are separate CLI deployments with existing functions and must not be replaced with HTML-only bundles. Main Git publication does not fix those sites or their historical deployments.
Technical checks: /entergy-property-rights-review resolves to the Entergy subdomain with HTTP 200 and no loop. All four sites serve HTTP 200 robots.txt and XML sitemaps. Entergy og:image and twitter:image are relative assets/og-cover.png; the image itself returns 200. Recommended later change: use https://entergy.winchlawfirm.com/assets/og-cover.png for both. No routing/canonical/robots changes or IndexNow submission performed.

## October 12, 2026 — top navigation and remaining phone references
Phone commit 639b8a5da688882e334db50f17fd77638e5033ea deployed as 6accd6df038433d91473563f, ready/published 12:47:38.929Z, verified live on home, consultation and Project Omega.
Added the explicitly requested “Entergy’s Babel-Webre Transmission Expropriations” and “Entergy’s Project Omega” links to the existing shared top navigation/mobile Menu, preserving all prior links. Destinations are https://entergybabelwebre.winchlawfirm.com/ and https://winchlawfirm.com/west-fork-creek/ . Updated consultation JavaScript error-message phones and phone-click contact_line classification to match the authorized assignments. Native menu button and navigation CSS/interaction remain intact. Build, 12-page checks, JavaScript syntax, menu open/close/aria-state simulation and both phone tracking cases passed. Browser rendering/click verification is unavailable because the supported browser runtime fails initialization; live href and destination HTTP checks are required after this commit.

## October 12, 2026 — accessible project dropdown
Replaced the three separate Entergy/project header links with an actual “Entergy Projects” disclosure button and dropdown containing all three destinations; all other navigation links remain. The mobile Menu contains the same dropdown. Native button supports Enter/Space and click/touch; ArrowDown/ArrowUp open and focus the first/last project link; Escape closes and restores focus; outside click and focus departure close the dropdown; closing the mobile menu closes the project list. Desktop list is positioned below its toggle; mobile list expands inline. Build and 12-page checks passed, JS syntax passed, and interaction simulation covered each close/open/focus path. Production and browser verification remain separate checks after this commit.


## October 12, 2026 — daily SEO + activity review
### Current measurement
- GA4 account `winchlawfirmgoogleanalytics` (`417150352`) returned an empty result for landing pages, sources, and events for 2026-09-14 through 2026-10-11. This remains an empty connector result, not zero traffic.
- The connected GA4 property `Property1` (`555762522`) returned 92 sessions and 60 active users in the same window. Homepage: 81 sessions, 60 active users, 47 engaged sessions (58.02% engagement). Google organic: 16 sessions, 14 active users, 14 engaged sessions (87.5% engagement). The recorded event totals included 5 `generate_lead` events marked as conversions, 2 `document_open` events with 1 marked conversion, 5 `form_start`, and 1 `form_submit`.
- Search Console returned 9 clicks, 100 impressions, and the current page rows show 8 homepage clicks from 72 impressions (11.11% CTR, average position 5.03), 17 Entergy-page impressions with 0 clicks (average position 3.88), and 1 click from 6 impressions on the utility-servitude article (average position 8.67).
- Neither GA4 nor Search Console returned usable preceding-period rows for 2026-08-17 through 2026-09-13, so no period-over-period percentage is asserted.

### Live inspection
- Main site and all three specialty homepages returned HTTP 200.
- Main site canonical, `og:url`, and social images are absolute.
- Entergy canonical and `og:url` are correct, but `og:image` and `twitter:image` remain relative (`assets/og-cover.png`).
- Babel-Webre has a canonical but no live Open Graph/Twitter tags.
- Business Legal has a canonical and form, but no live social-image tag was found.
- Entergy and Babel-Webre forms are present in the live HTML; receipt/notification delivery was not tested in this run. Robots and sitemap endpoints returned HTTP 200.

### Focused action
- PREPARED: added valid Article JSON-LD to `public/post/should-i-sign-utility-servitude-agreement-louisiana/index.html` in GitHub commit `03b62003660cdbce073dfe3e577a7f117936f666`. This targets the only currently measured substantive article with a click and a page-2-ish average position.
- Verification: GitHub source contains the schema. The currently published Netlify deploy is still commit `785b6594e7c0a34d4226ff68997b63215ba3b00c`; the live article does not yet contain the new JSON-LD. Therefore this is PREPARED, not DEPLOYED.

### Queue
- BLOCKED: main-site GitHub commit `03b6200...` has not reached the published Netlify deploy through the currently observed deployment connection.
- NEXT: trigger/repair the Git-to-Netlify production deployment, then fetch the article HTML and confirm the JSON-LD is live. After that, publish the specialty metadata patch and verify form receipt/notification.


## October 13, 2026 — measurement-chain reconciliation
### Where the analytics chain currently stops
- The live site loads Google Tag Manager container `GTM-PB4XQM3P`.
- The public GTM container resolves to measurement ID `G-TFD9CQT062`.
- GA4 data for that measurement ID is being returned under account/property `555762522`, display name `Property1`, stream `15838544994`.
- That stream recorded sessions across `winchlawfirm.com`, `www.winchlawfirm.com`, `entergy.winchlawfirm.com`, `entergybabelwebre.winchlawfirm.com`, and `businesslegal.winchlawfirm.com`.
- The named Windsor connection `winchlawfirmgoogleanalytics` (`417150352`) returned an empty result again for the same requested window. The stop is therefore after the website tag and GA4 collection, at the property/account mapping or permissions for the named Windsor connection—not at the website tag.

### Current activity, September 15–October 12
- Verified live GA4 fallback property: 90 homepage sessions, 67 active users, 53 engaged sessions (58.89% engagement); 16 Google-organic sessions with 87.5% engagement.
- Search Console: homepage 8 clicks / 72 impressions / 11.11% CTR / average position 5.03; Entergy page 17 impressions / 0 clicks / average position 3.88; utility-servitude article 1 click / 6 impressions / average position 8.67.
- No usable preceding-period rows were returned for GA4 or Search Console, so no period-over-period percentage is asserted.

### Action
- COMPLETE/VERIFIED: updated the daily automation with the verified measurement mapping and a required fallback to account `555762522`, while continuing to report `417150352` as empty. This prevents future runs from treating the wrong property as the live source.
- PREPARED: Article JSON-LD patch remains in GitHub but is not live. The current Netlify production deploy is a manual deploy titled `Correct U-37882 docket card destination only` and does not contain the patch.
- BLOCKED: direct deployment of the Article schema and specialty metadata through the current Netlify tool surface.

### Next queue
Repair the GitHub-to-Netlify production trigger or use an authorized manual deploy path, then verify the Article JSON-LD live. Separately reconcile/rename the GA4 property in Google so the live stream is no longer ambiguously labeled `Property1`.


## October 14, 2026 — persistent Article schema repair (COMPLETE/VERIFIED)
### Diagnosis superseding yesterday's deployment-blocker assumption
Netlify production deploy 6ace304829f2ee2aff7f5b3a was ready and published October 13 at 13:21:23Z from GitHub commit 88ab4a527f0928abf93169efa0ab6448938ee961. Thus Git-to-Netlify publication is functioning for the main site. The prior patch edited generated public HTML, but build.py regenerated that file without Article JSON-LD. This was a generator omission, not demonstrated missing deployment permission or a broken Git trigger. Do not repeat the stale main-site deployment blocker.

### Executed fix and evidence
- Commit 6524ddbba3a127a0e24ab35b65f118dc534e4e87 updates build.py to generate Article JSON-LD on the utility-servitude guide and adds a regression test in tests/check_site.py.
- Schema is generated from the same origin/path/title/description as the page: canonical, mainEntityOfPage, Article @id, and absolute image cannot silently diverge. No author biography, publication date, review rating, or legal outcome was invented.
- Two local rebuilds passed: all 12 HTML documents, HTTPS/internal routes/assets, form markup, existing phone lines, retained articles, crawl files, JavaScript syntax, and exactly one matching Article schema. These are build/structure tests, not end-to-end form delivery or browser rendering tests.
- Production deploy 6acf837a0f9182bdceddee1f: state ready, commit 6524ddbba3a127a0e24ab35b65f118dc534e4e87, published 2026-10-14T13:28:37.374Z. Live HTTPS article returned 200 and parsed Article JSON-LD matching its canonical, visible H1 and og:image.
- No phone assignments, legal article body, navigation, forms, or specialty deployments changed. October 12 user-authorized numbers in AGENTS.md supersede reversed historical records: general/main/Business Legal 504-377-2620; Entergy/Babel/Omega 504-500-1899.
- Benefit: this metadata now survives future builds. No ranking/rich-result or inquiry gain is claimed.

### Current measurement (September 16–October 13, inclusive)
- Requested property 417150352 returned [] for current landing/source/event reports and prior totals. Cause for that property's empty report remains unproven; its emptiness does not establish zero traffic or broken collection on the live property.
- Verified live property 555762522: aggregate 118 sessions, 82 active users, 63 engaged sessions. This is unfiltered and includes development/testing hosts; do not describe all as prospective clients.
- Google organic: 17 sessions, 15 engaged. Direct mail / qr: 2 sessions, 2 engaged. Events: generate_lead 6 (6 key events), document_open 4 (2 key events), form_start 6, form_submit 1. These do not prove six real inquiries, PDF receipt, or qualified matters.
- Host + landing report: main apex /west-fork-creek 9 sessions/5 active users/7 engaged; Entergy root 14/10/11; Babel root 10/5/8; Business Legal root 6/5/5. Sessions/users across host/page breakdowns are not necessarily additive.
- Search Console page rows: 10 clicks and 110 impressions summed across returned pages; homepage 8/74 (10.81% CTR, position 4.99), Entergy 0/18 (position 3.72), utility-servitude guide 1/6 (position 8.67), historic HTTP Babel 1/1. Query rows expose 3 branded clicks for justin winch, but not all queries; no intent is inferred for omitted queries.
- Preceding August 19–September 15 reports returned [] for live-property GA4 totals and GSC pages; no percentage growth is calculated.

### Public audit and remaining queue
- All four root pages and their robots.txt/sitemap.xml endpoints returned 200. Sitemaps were XML and robots files point to their own site's sitemap.
- Main article/contact/Omega routes returned 200 with matching canonical/og:url, absolute social-image addresses, GTM and viewport markup.
- Viewport markup is not a substitute for visual mobile QA; no browser-rendered mobile test was performed.
- PREPARED/BLOCKED: specialty social tags remain unfinished. Entergy social images remain relative; Babel lacks og:url/social-image tags; Business Legal lacks a social-image tag in today's HTML. Current Netlify tool surface lacks a direct deploy/create/upload operation; this is an exposed-tool limitation, not proof that the account's OAuth permissions are read-only. Preserve existing specialty functions and do not upload HTML-only replacements.
- NEXT: verify actual consultation/PDF receipt and notification through the intended intake destination; then complete specialty social metadata when a supported publication path is available.

### Five-minute creative candidate (internal draft; not published or mailed)
A small document-checklist insert for the existing landowner letter: "Received a utility notice? Keep the letter, proposed agreement, map and any appraisal together." Audience: recipients already reviewing a utility acquisition; purpose: make the next step practical, not alarming. Proposed campaign link: https://entergy.winchlawfirm.com/?utm_source=direct_mail&utm_medium=qr&utm_campaign=notice_review_2026_10#reviewForm . This is a draft campaign convention, not a claim that letters have been mailed or the QR was scanned. Incremental printing cost is unknown; no spending/contact/publication occurred. Next small action: generate and camera-test this campaign's QR before any print batch, logging synthetic tests separately from recipient activity.

### Sprint record
Completed within the 30-minute cap: current/prior measurement reads, public endpoint audit, generator diagnosis, narrow source/test patch, two builds, Git commit, production-deploy and live-schema verification, and the unsent checklist/QR candidate. No fabricated per-minute work durations are asserted.

## October 16, 2026 — public-use opinion article
User authorized publication of the Nguyen opinion blog. Prepared a new article at /post/west-fork-creek-public-use-supreme-court using the existing shared design and Article schema; added it to the existing Articles and Resources listings and sitemap. Preserved both earlier articles and existing forms, navigation, analytics and phone assignments. Links include the official March 6, 2026 Supreme Court opinion, the utility statute, and the existing West Fork Creek resource. Distinguishes the port holding from utility-specific analysis. Publication and live verification are pending this commit.
