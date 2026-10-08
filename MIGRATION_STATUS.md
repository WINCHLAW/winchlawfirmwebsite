# Migration status — 2026-10-08
## Verified live update — October 8, 2026, morning
Netlify plugin and direct HTTPS checks now confirm the main site is published at https://winchlawfirm.com/ on project majestic-cajeta-b5cfbd (50259f63-1a06-4d44-80b1-36fe24a8e725). Production deploy 6ac79c58b81b99000808ed1a published at 2026-10-08T13:36:39Z from WINCHLAW/winchlawfirmwebsite main commit e30abec732b01da371378ef5fa3c0988bbaa2286. Earlier statements below about Wix remaining live and no Netlify plugin are historical and superseded by this evidence. Do not rebuild or re-import the site.

Today's bounded priority is consultation capture: the live /book-online form has Netlify markup, but form processing was disabled and Netlify listed no forms. Enabled Netlify Forms through the authorized plugin; this commit requests a Git-connected rebuild to detect the form. Registration, synthetic submission storage, notification delivery and upload receipt are not yet verified. Do not call the form fully working solely from a 200 response or the enabled setting.

Analytics September 10–October 7 compared with August 13–September 9: requested GA4 property 417150352 completed with no rows; separately connected property 555762522 (Property1) returned 53 sessions, 41 active users, 25 engaged sessions, 47.17% engagement. Its hostname/source/landing report includes 8 google/organic sessions on www.winchlawfirmllc.com and 2 on www.winchlawfirm.com. No consultation/contact key-event rows; all returned key-event counts zero. Prior-period reads completed empty; do not claim percentage growth from those results. This reconciles the native GA activity with the formerly empty specified property. Property1 also includes deploy-preview hostnames; do not call all sessions qualified leads.

Search Console sc-domain:winchlawfirm.com, same recent 28-day range including provisional fresh data: HTTPS www homepage 6 clicks/56 impressions/10.71% CTR/position3.3214; HTTP Babel 1/1/100%/1; HTTP www 0/2/0%/6.5; HTTPS Entergy 0/12/0%/3.6667. Query rows expose 3 clicks for 'justin winch'; anonymized omitted queries prevent classifying all clicks. Prior period returned no rows.

Specialty live checks: Entergy canonical and og:url now correctly https://entergy.winchlawfirm.com/; og:image and twitter:image remain assets/og-cover.png. Babel canonical now correctly https://entergybabelwebre.winchlawfirm.com/, but Open Graph/Twitter tags absent. Dedicated expropriation +15043772620 preserved. Specialty metadata completion remains pending after inquiry-capture repair.

Queue: navigation reported complete October2 and verified October7; do not repeat installation. Main consultation processing repair in progress today; next gate stored synthetic inquiry and firm notification receipt. Specialty social metadata then robots/sitemap verification pending. Eagle adoption remains research-only, no spending/outreach/publication authorized for this sprint.

## Prepared — West Fork Creek / Project Omega landing page
Added a verified-information landing page at `/west-fork-creek` describing the West Fork Creek–Boeuf / Project Omega corridor and its related LPSC terminology (West Fork Creek–St. Landry). The page links to LPSC Docket U-37882, Order No. U-37882, public transmission testimony, Entergy’s project announcement, and the available interactive map. The page is prepared and locally checked; it is not yet deployed.
## Current state
Source committed to GitHub main at e3b92110d27a70fd794deea4c78da9fbe65e5a10 and confirmed by fetching origin/main. Netlify secure sign-in request returned declined on 2026-10-07; no deployment performed. Resume from authenticated Netlify access, not another rebuild.
Main live site remains Wix at https://www.winchlawfirm.com/. No DNS or specialty-site changes made.
Replacement rebuilt as static HTML/CSS/JS; Wix platform internals are not portable source. Existing main-page content and both published articles were retrieved from their live URLs, with sanitized source content in migration/.
Local build includes ten page routes (eight indexed), preserved article paths, landowner resource, resource directory, functional-form markup, static eagle, mobile menu, absolute share images/canonicals, robots/sitemap, old Entergy path redirects.
Homepage outcome-multiple language omitted from replacement; original remains in migration/home.html for review. Empty Wix booking service replaced with a consultation-request form, not a scheduling promise. Newsletter signup/member notifications are not migrated as services; legacy notifications redirects to contact.
## Verified locally
Build succeeds. Source link/metadata checks and JS syntax checks are recorded in tests/LOCAL_CHECKS.md. Browser rendering, Netlify form processing, notifications, and GA receipt are not verified.
## Exact blockers / launch gates
1. Netlify available browser is signed out. No Netlify plugin surfaced in discovery. Need authenticated account to create a separate main-site project connected to WINCHLAW/winchlawfirmwebsite, branch main, netlify.toml settings.
2. Enable form detection, deploy, configure consultation email notifications to justin.winch@winchlawfirm.com, and verify a synthetic request with dummy PDF reaches Netlify and firm inbox. Never assume delivery from an HTTP200 alone.
3. Correct GA4 property/measurement ID must be verified. Prior Windsor property417150352 returned no rows; user screenshot shows property555762522. Existing Wix public HTML did not reveal a GA measurement ID. GA_MEASUREMENT_ID is intentionally unset. Tracking code supports phone_click/email_click/specialty_site_click/consultation_start/generate_lead; GA receipt/key-event configuration pending.
4. Verify desktop and mobile preview, every preserved route, specialty link, images, form error states and no overflow. Article illustration should be archived at full resolution before retiring Wix.
5. Preserve email MX/TXT and all specialty-subdomain DNS; change only main web routing after gates pass. HTTPS certificate, www/apex redirect, canonical URL, and rollback must be tested.
6. Make a harmless repository change and observe the subsequent live Netlify deployment before claiming Git delivery works.
## Existing content
/ — main site
/louisiana-landowner-bill-of-rights — retained text
/legal-resources — directory enhanced with existing resources
/blog — both article links
/post/received-utility-right-of-way-offer-letter-louisiana — retained
/post/should-i-sign-utility-servitude-agreement-louisiana — retained
/book-online — consultation request instead of empty booking page
## Not part of this migration
Specialty sites are not modified. Their previously identified robots/sitemap, canonical/share metadata, intake/tracking issues remain a separate queue. Do not treat main migration as proof those sites work.
