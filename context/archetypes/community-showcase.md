# Story Archetype: Community Showcase

Celebrating user achievements and building ecosystem engagement.

## When to Use

- Community member builds something impressive
- Novel use case discovered
- Open source contribution
- Successful implementation story
- Teaching/educational content created

## Narrative Structure

### Act 1: The Builder and Their Project (25%)

**Who and what**
- Introduce the person/team
- What they built or accomplished
- Why they chose Amplifier
- What problem they were solving

**Example:**
"Sarah Chen, a solo developer building an AI-powered code review tool, needed a way to coordinate multiple specialized agents. She turned to Amplifier and built CodeSentinel - an autonomous code review system that runs security, performance, and style analysis in parallel."

### Act 2: Their Approach (35%)

**How they did it**
- Which Amplifier capabilities they used
- Interesting patterns or techniques
- Challenges they overcame
- Creative solutions

**Example:**
"Sarah's approach: Use recipe workflows to orchestrate 5 specialized agents (security-guardian, zen-architect, bug-hunter, test-coverage, python-code-intel). Each agent analyzes the PR independently, then a consolidator agent synthesizes findings into one coherent review.

The clever part: She used approval gates in the recipe so critical security findings pause the review for human judgment before posting."

### Act 3: The Results (25%)

**What they achieved**
- Metrics and outcomes
- User feedback or adoption
- Impact on their project/business
- Unexpected benefits

**Example:**
"Results: Code review time dropped from 2 hours to 15 minutes. Security issues caught 95% of the time (vs 40% with manual review). The team's PR velocity doubled. 'It's like having a senior developer review every PR instantly,' Sarah says."

### Act 4: The Takeaway (15%)

**What others can learn**
- Applicable patterns
- Try it yourself instructions
- Links to their work (if open source)
- Call to action for community

**Example:**
"Sarah's recipe is open source: github.com/user/codesentinel

Key patterns you can reuse:
• Multi-agent orchestration with recipes
• Approval gates for critical decisions
• Result consolidation patterns

Want to build something similar? Start with foundation:zen-architect and security-guardian agents."

## Slide/Section Mapping

### For Blog Post (600-900 words)
- **Title:** "[User] Built [Project] with Amplifier"
- **Introduction** (100 words) - Who and what
- **The Challenge** (150 words) - Problem they faced
- **The Solution** (350 words) - How they used Amplifier
- **The Results** (150 words) - Impact and metrics
- **Try It** (150 words) - Links and call to action

### For PowerPoint (8-12 slides)
1. **Title** - "[Project] by [User]"
2. **The Builder** - Who they are, what they're building
3. **The Challenge** - Problem they needed to solve
4. **The Solution** - Amplifier capabilities used
5. **How It Works** (2-3 slides) - Their approach with examples
6. **The Results** - Metrics and impact
7. **Key Patterns** - What others can learn
8. **Try It** - Links and resources

### For Social Media
**Twitter Thread:**
```
1/ 🌟 Community Spotlight: @user built [project] with Amplifier!

2/ The challenge: [brief problem]

3/ The solution: [which Amplifier capabilities]

4/ The results: [key metric] 

5/ What's impressive: [specific innovation]

6/ Try it: [link] | Learn more: [link]
```

**LinkedIn:**
```
I'm excited to spotlight [User] and their [Project] built with Amplifier! 🚀

[Brief description of what they built]

The problem they solved:
[Pain point]

Their approach:
[Amplifier capabilities + creative implementation]

The results:
• [Metric 1]
• [Metric 2]
• [Metric 3]

This is the power of the Amplifier ecosystem - enabling developers to build
sophisticated AI agent systems that would take months from scratch.

Check out their work: [link]

#AIEngineering #OpenSource #DeveloperTools
```

## Showcase Discovery

### Where to Find Community Projects

**GitHub Search:**
```bash
# Repos using Amplifier
gh search repos "amplifier" --limit 50

# Recent repos importing Amplifier
gh search code "from amplifier import" --language python
```

**Social Media:**
- Search #amplifier, #amplifierai
- Monitor @mentions
- Track GitHub stars

**Community Channels:**
- GitHub Discussions
- Discord servers
- Twitter/LinkedIn shares

### Showcase-Worthy Criteria

**Must have:**
- Real working project (not just experimentation)
- Creative or novel use of Amplifier
- Measurable results or impact
- User willing to share (public repo or explicit permission)

**Bonus points:**
- Open source contribution back to Amplifier
- Solves interesting problem
- Novel integration or pattern
- Educational value for community

## Writing Principles

### Celebrate, Don't Promote
Focus on the user's achievement, not Amplifier's features:
- "Sarah built an amazing code review tool" ✓
- "Amplifier enables code review tools" ✗

### Be Specific
Vague praise doesn't inspire:
- "Reduced review time from 2 hours to 15 minutes" ✓
- "Made code review much faster" ✗

### Make It Actionable
Readers should be able to:
- See the code/project
- Understand the approach
- Try similar patterns themselves
- Connect with the builder

### Give Proper Credit
- Use real names (with permission)
- Link to their GitHub/social media
- Quote them directly
- Acknowledge contributions

## Templates to Use

### Word Case Studies
```javascript
const { createCaseStudy } = require('./templates/case-study-template');

createCaseStudy(
  'CodeSentinel: AI Code Review with Amplifier',
  'Challenge: Manual code review couldn\'t keep pace with team velocity...',
  'Solution: Multi-agent orchestration with recipes for parallel analysis...',
  'Results: 87% faster reviews, 95% security issue detection...'
);
```

### PowerPoint Showcases
Use templates:
- `slide-title.html` - Project name and builder
- `slide-content.html` - Challenge and approach
- `slide-comparison.html` - Before/after metrics
- `slide-code.html` - Key implementation patterns
- `slide-metrics.html` - Impact numbers

## Integration with Community Manager

This archetype is primarily used by the `community-manager` agent to:
- Celebrate user achievements
- Highlight creative applications
- Build ecosystem awareness
- Inspire others to contribute and share

## Checklist

Before publishing a Community Showcase:
- [ ] User permission obtained (if not already public)
- [ ] Project link works and is accessible
- [ ] Metrics are accurate
- [ ] User is properly credited
- [ ] Technical details are correct
- [ ] Includes "try it yourself" resources
- [ ] Encourages community engagement
- [ ] Cross-posted to relevant channels

## Success Criteria

Community showcase succeeds when:
- Featured user feels proud and appreciated
- Others are inspired to build or contribute
- Community engagement increases (stars, forks, discussions)
- Demonstrates Amplifier's versatility
- Drives ecosystem growth

---

**Reference:** This archetype builds community and showcases real-world Amplifier applications.
