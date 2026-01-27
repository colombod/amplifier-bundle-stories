# Story Archetype: Feature Journey

Exploratory narrative for complex features with interesting development stories.

## When to Use

- Complex features with non-obvious solutions
- Architectural decisions with trade-offs
- Features that evolved significantly during development
- Stories where the "how we got there" is interesting

## Narrative Structure

### Act 1: The Starting Point (20%)

**Where we began**
- Initial problem or opportunity
- Early assumptions
- What we thought would work
- Constraints and requirements

**Example:**
"We needed a way for agents to share reusable capabilities. Initial thought: just use MCP tools. But we quickly realized MCP tools lacked semantic typing - you couldn't tell what a tool actually DID without reading its description."

### Act 2: The Journey (50%)

**What we tried and learned**
- First approach and why it didn't work
- Second approach and its limitations
- Key insights that changed our thinking
- Breakthrough moments
- Design iterations

**Example:**
"First attempt: Wrap MCP tools with metadata. Problem: Still required 1,500 lines of boilerplate per capability.

Second attempt: Use Python type hints to generate tool definitions. Better, but coupling was too tight.

The breakthrough came during a session debugging Surface: what if the semantic types WERE the interface? The tool definition could be GENERATED from the type signature. This inverted the whole model."

### Act 3: The Breakthrough (20%)

**The solution that worked**
- What we finally built
- Why it succeeded where others failed
- Key design decisions
- The "aha moment"

**Example:**
"Surface became the 6th module type - semantic capability contracts that generate MCP tool definitions. The type signature IS the interface. Implementation stays separate. 60% less YAML, pip-installable, discoverable by AI agents."

### Act 4: Reflection (10%)

**What we learned**
- Lessons about the problem domain
- Unexpected benefits
- What we'd do differently
- Implications for future work

**Example:**
"Key learning: The right abstraction inverts complexity. We tried to wrap the complex thing (MCP tools). The breakthrough was finding a simpler thing (Python types) that GENERATES the complex thing. Complexity doesn't disappear - it just moves to where it belongs."

## Slide/Section Mapping

### For PowerPoint (15-20 slides)
1. **Title** (1 slide)
2. **Context** (2 slides) - Problem + initial approach
3. **Journey** (8-10 slides) - Iterations, learnings, dead ends
4. **Breakthrough** (3-4 slides) - Final solution with examples
5. **Reflection** (2-3 slides) - Lessons, implications

### For Word (2000-3000 words)
- **Introduction** (200 words) - Hook + context
- **The Starting Point** (400 words) - Problem and first assumptions
- **The Journey** (1200 words) - Iterations with code examples
- **The Breakthrough** (600 words) - Solution and design
- **Reflection** (300 words) - Learnings and future
- **Appendix** (300 words) - Technical details, references

### For Blog Post (1000-1500 words)
- **Hook** (150 words) - Opening with interesting moment
- **The Challenge** (250 words) - What we faced
- **The Exploration** (500 words) - Key iterations and insights
- **The Solution** (350 words) - What worked and why
- **Lessons** (250 words) - What we learned

## Key Principles

### Embrace the Messiness
Don't hide the dead ends and mistakes. They make the story relatable and the breakthrough more satisfying.

### Show the Thinking
Explain WHY you tried each approach and why it didn't work. The reasoning process is often more valuable than the final solution.

### Focus on Insights
Each iteration should teach something:
- "We learned that X doesn't work because Y"
- "This revealed that Z was the real problem"
- "The key insight was realizing A and B are actually the same thing"

### Make the Breakthrough Satisfying
The reader should understand why the final solution works where others failed. The "aha moment" should be clear.

## Timeline Elements

Include specific timeline markers:
- "Week 1: Initial implementation"
- "Day 3: First major pivot"
- "Two weeks in: The breakthrough"
- "Final week: Testing and refinement"

Timelines make the journey concrete and show velocity.

## Code Evolution

Show how the code changed through iterations:

**Iteration 1:**
```python
# First approach - manual wrapping
def create_tool(name, description, handler):
    return {
        "type": "function",
        "function": {
            "name": name,
            "description": description,
            # ... 50 more lines of boilerplate
        }
    }
```

**Iteration 2:**
```python
# Second approach - decorator
@mcp_tool(description="...")
def my_capability(...):
    ...
# Still verbose, still manual
```

**Final Solution:**
```python
# Breakthrough - semantic types generate everything
class FileSearch(Surface):
    query: str
    file_types: list[str]
    # Tool definition generated automatically
```

## Checklist

Before publishing a Feature Journey story:
- [ ] Journey has clear phases (starting point, explorations, breakthrough)
- [ ] Each failed approach has a clear "why it didn't work"
- [ ] Breakthrough moment is identified and explained
- [ ] Code examples show the evolution
- [ ] Timeline provides concrete pacing
- [ ] Lessons are explicit and actionable
- [ ] Final solution is clearly superior to alternatives
- [ ] Reader understands the problem domain better

## Examples

**Good headlines for this archetype:**
- "Building Surface: The 6th Module Type Journey"
- "How We Made Recipes Resumable: A Deep Dive"
- "From Concept to Production: The Session Forking Story"

**Good journey moments:**
- "We thought we needed X, but discovered Y was the real problem"
- "The third attempt failed, but revealed the key insight"
- "After two weeks of exploration, everything clicked"

---

**Reference:** This archetype works well for features with interesting development stories, not just straightforward implementations.
