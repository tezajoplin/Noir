# NOIR --- Master Project Brief & AI Development Instructions

> Single source of truth for building the NOIR website. Read this before
> making significant design, UX, content, architecture, or development
> decisions.

## 01 --- Project

NOIR is a premium custom sportswear brand originating from Pontianak,
West Kalimantan.

The website is a **brand-first experience**, not an e-commerce-first
website.

The website should help sports communities and teams discover NOIR,
understand what it stands for, see real work and real people, explore
the sports/products NOIR serves, understand the process, and eventually
start a project / request a quote.

NOIR should not feel like a generic jersey manufacturer or a generic
sportswear ecommerce template.

## 02 --- Brand DNA

### Purpose

NOIR exists because every football community deserves an identity they
can proudly wear.

West Kalimantan has a deep-rooted football culture. New communities and
teams are constantly formed, yet many still rely on generic jersey
templates with only their team name added.

A jersey should represent more than a name --- it should represent who
the team is.

NOIR exists to help sports communities build an identity that truly
reflects their character. Through thoughtful design, reliable
craftsmanship, fast production, and competitive pricing, NOIR aims to
make custom sportswear accessible without compromising quality.

### Positioning

> **We build team identities, not just jerseys.**

NOIR sells identity through custom sportswear.

The deeper value is: - Identity - Pride - Belonging - Community -
Representation

### Core Philosophy

> **More Than a Jersey. It's Who We Are.**

Do not repeat this line unnecessarily throughout the website.

### Target Market

**Primary:** Football communities in West Kalimantan.

**Secondary:** Local football teams, football academies, futsal teams,
schools, companies, and other sports communities.

### Values

**Identity First** --- Every product should strengthen a team's
identity, not just fulfill an order.

**Quality Matters** --- Materials, craftsmanship, and finishing matter.

**Customer Partnership** --- NOIR works together with customers to bring
their vision to life.

**Continuous Improvement** --- Products, services, and processes should
continuously improve through feedback and innovation.

## 03 --- Design Direction

The website should feel: - Simple - Elegant - Premium - Editorial -
Spacious - Image-led - Modern - Confident - Refined - Human -
Practical - Purposeful

The visual environment should primarily be **light / white-based**.

Premium should come from **composition, typography, photography,
spacing, hierarchy, and restraint** --- not decoration.

### Avoid

Do NOT drift toward: - Generic sports-template aesthetics - Generic
ecommerce layouts - SaaS-style card grids - Excessive rounded cards -
Excessive borders or shadows - Excessive gradients - Dark/gothic
treatment - Excessive gold - Decorative UI - Repetitive cards -
Repetitive image + text blocks - Unnecessary animations - Over-designed
navigation - "AI-generated website" aesthetics - Visual complexity for
the sake of looking premium

> **Use fewer, stronger elements.**

Whitespace is intentional. Do not add elements merely because an area is
empty.

## 04 --- Photography & Product Rules

Real photography is preferred whenever available.

Real product photography is the **source of truth** for products.

Never invent or alter: - Logos - Sponsors - Badges - Typography - Jersey
patterns - Names - Numbers - Product construction

If a supplied image shows a real product, preserve the actual product
design.

Do not invent product specifications or visual details.

Photography should feel integrated into the page rather than trapped
inside generic rectangular cards.

Prefer: - Large editorial crops - Seamless white/off-white transitions -
Natural image edges - Controlled cropping - Strong negative space -
Image-led layouts - Subtle fades

Avoid: - Hard rectangular boundaries when unnecessary - Image cards with
unnecessary borders - Decorative frames - Generic image placeholders

## 05 --- Homepage Strategy

The homepage is **brand-first**.

The intended progression is:

**Identity → Story → Proof → Community → Lifestyle → Products → Process
→ Conversion**

Products should feel like a natural expression of the NOIR brand, not
the reason the homepage exists.

Every section must have a clear job.

Do not create a generic "Why NOIR" section.

Prefer real proof through real projects, real people, photography,
actual process, and relevant product information.

Do not repeat the same card/grid pattern throughout the homepage.

## 06 --- Locked Homepage Structure

### 01 --- HERO

Primary statement:

> **WE BUILD TEAM IDENTITIES, NOT JUST JERSEYS.**

Use strong product/craft/player/team imagery.

Primary CTA:

**START A PROJECT**

Keep the Hero immersive, premium, editorial, and uncluttered.

### 02 --- THE STORY

Headline:

> **EVERY TEAM HAS A STORY.**

Core message:

> A jersey can carry a name.\
> But the right jersey carries something more.\
> Identity. Pride. Belonging.

Purpose: explain why the jersey matters before moving into proof.

The section should be light, spacious, and seamless. Photography should
blend naturally into the white page rather than appearing as a hard
rectangular block.

**This section has already been manually refined and should not be
redesigned unnecessarily.**

### 03 --- BUILT WITH NOIR

Featured project:

> **PERSIWAH FC**

Preferred structure: - Large project image on the left - Project
information on the right - Supporting projects below when appropriate

The project image should remain the hero. Do not turn it into a generic
portfolio card grid.

### 04 --- COMMUNITY

Headline:

> **MADE FROM PONTIANAK.**\
> **WORN BY THE COMMUNITY.**

Use the selected real community photograph.

Preferred composition: - Text on the left - Main image on the right -
Clean alignment - Do not push content unnecessarily to the extreme edges

Section 04 and Section 05 should feel like one continuous visual chapter
while remaining separate semantic sections.

Avoid excessive spacing between them.

Optional small metadata above the image:

> PONTIANAK / WEST KALIMANTAN

Do not add unnecessary captions.

### 05 --- LIFESTYLE

Headline:

> **MADE FOR THE PITCH.**\
> **WORN EVERYWHERE ELSE.**

Use one strong editorial lifestyle photograph --- the selected group
photo on the stairs.

Preferred composition: - Large image on the left - Text on the right -
Text visually balanced/centered in its area - No supporting gallery

Optional small metadata:

> ON THE PITCH / OFF THE PITCH

Do not add unnecessary captions.

### 06 --- WHAT WE MAKE

Headline:

> **BUILT FOR EVERY SPORT WE SERVE.**

This is **not** a conventional rectangular category-card grid.

#### Approved concept

Use a large real rear-view football photograph as an
environmental/background visual, occupying approximately 50--70% of the
section.

Chosen image: rear-view red football jersey with **TEZA / 3**.

Target image scale: approximately **120--125%**.

The subject should sit slightly toward the **left**, leaving visual
breathing room on the right for the product catalogue.

Starting CSS values can be around: - `transform: scale(1.2)` -
`object-position: 38% center`

These are starting points, not immutable values.

The image must feel like part of the environment, not a rectangular
card.

Use an extremely smooth white fade where needed.

Avoid: - Hard image boundaries - Rectangular image boxes - Heavy
borders - Large horizontal dividers - Obvious section containers

#### Product catalogue

Primary visual categories: 1. **Football** 2. **Futsal** 3.
**Basketball**

Football is visually dominant.

Use real product/team photography where available and restrained links
such as:

> VIEW COLLECTION →

Do not repeat the same generic card structure for every sport.

#### More Products

Do not force Badminton into the main visual catalogue if suitable real
photography is unavailable.

Use a secondary **MORE PRODUCTS** area for: - Padel - Badminton -
T-Shirts - Jackets - Training Wear - Lifestyle - Accessories

#### Floating jersey assets

When used: - One jersey per asset - Prefer front-facing/natural upright
orientation - Realistic fabric folds - Subtle studio lighting -
Transparent background where appropriate - No mannequin - No person - No
hanger - No props - No invented text - No altered logos/sponsors -
Preserve the exact supplied jersey design

Floating jerseys are product statements, not generic 3D decoration.

### 07 --- HOW IT WORKS

Headline:

> **FROM IDEA TO IDENTITY.**

Process: 1. **Discover** --- Understand the team, community, sport,
identity, and requirements. 2. **Design** --- Translate the team's
identity into a custom design. 3. **Produce** --- Turn the approved
design into the finished sportswear. 4. **Wear** --- The final product
becomes part of the team's identity on and off the field.

Keep this section simple and friction-reducing. Avoid generic SaaS
process-diagram styling.

### 08 --- FINAL CTA

Headline:

> **YOUR TEAM.**\
> **YOUR IDENTITY.**\
> **LET'S BUILD IT.**

Supporting line:

> Tell us what your team stands for.

Primary CTA:

> **START A PROJECT**

The closing section should feel like the final page of a premium
editorial/company presentation, not a generic form card.

## 07 --- Primary Site Structure

Main navigation: - Home - Products - Football - Futsal - Basketball -
Badminton - Our Teams - How It Works - Insights - About - Get a Quote

SEO purpose: - **Home:** Introduce the brand and guide users to
important sections. - **Products:** Target commercial-intent searches
and showcase products by sport. - **Our Teams:** Build trust through
real projects, social proof, and case studies. - **How It Works:**
Reduce purchase friction and improve conversion. - **Insights:** Capture
informational search intent and build topical authority. - **About:**
Strengthen brand credibility and support E-E-A-T. - **Get a Quote:**
Convert visitors into qualified leads.

SEO should support the experience, not dictate the design.

## 08 --- Content Rules

Never invent factual business information.

Do NOT invent: - Product specifications - Fabric characteristics -
Production capabilities - Turnaround times - Minimum order quantities -
Awards - Client claims - Statistics - Testimonials - Achievements -
Partnerships - Manufacturing claims

If information is unknown, ask or use a clearly marked placeholder.

Real information is more important than making the website look
complete.

## 09 --- Astro 6 Development Rules

The project uses **Astro 6**.

Prefer: - Semantic HTML - Reusable components - Simple architecture -
Accessible interactions - Responsive layouts - Minimal JavaScript -
Maintainable CSS - Performance-conscious implementation

Do not introduce a library or dependency unless there is a clear reason.

Do not over-engineer.

Do not rebuild working sections just because another implementation is
possible.

## 10 --- AI Working Rules

### Core rule

> **Implement decisions. Do not independently redefine the NOIR brand.**

Before making a significant change: 1. Inspect the current
implementation. 2. Understand the existing structure. 3. Check this
document. 4. Identify what is locked/approved. 5. Determine the smallest
appropriate change. 6. Explain the intended change. 7. Explain important
trade-offs when relevant. 8. Implement only when the direction is clear.

If a proposed change conflicts with an approved direction, stop and ask.

### Never assume

Never assume: - The current code structure - A section should be
redesigned - A missing image should be replaced with invented imagery -
More animation is better - More cards are better - More content is
better for SEO - A generic "premium" pattern fits NOIR

Inspect first.

### Change scope

When asked to modify one section: - Modify that section first. -
Preserve unrelated approved sections. - Avoid large refactors unless
necessary. - Avoid changing the entire design system to solve a local
problem.

### Simplicity test

When two solutions achieve the same result, choose the simpler one.

When choosing between **more elements** and **fewer, stronger
elements**, choose fewer, stronger elements.

When choosing between **visual complexity** and **visual restraint**,
choose restraint.

## 11 --- Responsive Design

Desktop and mobile are both first-class experiences.

Do not simply shrink the desktop design.

For mobile: - Preserve hierarchy - Preserve the intended narrative -
Reorder only when necessary - Maintain readable typography - Prevent
image crops from destroying the subject - Avoid horizontal overflow -
Maintain comfortable spacing - Keep CTAs usable

Editorial/asymmetric desktop layouts should become simple and clear on
mobile.

## 12 --- Accessibility

Use: - Semantic HTML - Correct heading hierarchy - Descriptive alt
text - Accessible links/buttons - Keyboard-accessible interactions -
Sufficient contrast - Reduced-motion considerations where appropriate

Do not sacrifice accessibility for visual effects.

## 13 --- Performance

Prefer: - Optimized images - Correct image dimensions - Lazy loading for
below-the-fold imagery where appropriate - Minimal client-side
JavaScript - CSS over JavaScript when CSS can achieve the same effect -
No unnecessary third-party scripts

Large photography is central to the NOIR experience, so image
performance matters.

## 14 --- Current Project Status

### Approved / stable

**Section 01 --- Hero:** Direction approved.

**Section 02 --- The Story:** Manually refined and considered
acceptable. Do not redesign unless specifically requested.

**Section 03 --- Built With NOIR:** Persiwah FC is the featured project.
Direction approved.

**Section 04 --- Community:** Direction approved. Use the selected real
community photograph.

**Section 05 --- Lifestyle:** Direction approved. Use the selected
strong lifestyle photograph.

**Section 06 --- What We Make:** Direction approved,
implementation/design still being refined: - Large rear-view football
image - Approximately 120--125% scale - Subject slightly left - Seamless
white fade - Football / Futsal / Basketball as primary visual
catalogue - More Products for secondary categories - Floating jersey
assets where appropriate - No generic rectangular card grid

**Section 07 --- How It Works:** Content direction approved.

**Section 08 --- Final CTA:** Content direction approved.

## 15 --- Final Creative Standard

The NOIR website should feel like:

> **A premium sportswear brand with a strong local identity and real
> community behind it.**

It should NOT feel like: - An AI website - A generic jersey supplier - A
template - A sports ecommerce catalog - A SaaS landing page - A design
experiment

The strongest design language should come from:

**Photography + Typography + Whitespace + Composition + Restraint**

not decorative UI.

## 16 --- Default Behavior When Uncertain

If something is unclear:

**Do not invent.**

If a design decision is not locked:

**Propose options and explain the trade-off.**

If a section is already strong:

**Leave it alone.**

If a simpler solution works:

**Use the simpler solution.**

If real photography is available:

**Prefer the real photography.**

If a product detail is unknown:

**Ask rather than fabricate.**

If a visual element does not serve a clear purpose:

**Remove it.**

> **NOIR is built around identity. The website should make that identity
> felt through restraint, real people, real work, and purposeful
> design.**
