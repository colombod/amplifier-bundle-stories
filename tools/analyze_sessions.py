#!/usr/bin/env python3
"""
Analyze Amplifier sessions to identify problem-solving approaches and patterns.
"""

import json
import os
from pathlib import Path
from datetime import datetime
from collections import defaultdict, Counter
from typing import Dict, List, Any
import re


class SessionAnalyzer:
    def __init__(self, projects_dir: str):
        self.projects_dir = Path(projects_dir)
        self.sessions = []
        self.patterns = defaultdict(list)

    def find_all_sessions(self) -> List[Path]:
        """Find all session metadata.json files."""
        metadata_files = []
        for root, dirs, files in os.walk(self.projects_dir):
            if "metadata.json" in files and "sessions" in root:
                metadata_files.append(Path(root) / "metadata.json")
        return sorted(metadata_files)

    def parse_metadata(self, metadata_path: Path) -> Dict[str, Any]:
        """Parse session metadata."""
        try:
            with open(metadata_path, "r") as f:
                data = json.load(f)
            return data
        except Exception as e:
            print(f"Error parsing {metadata_path}: {e}")
            return {}

    def parse_transcript(self, session_dir: Path) -> List[Dict[str, Any]]:
        """Parse session transcript."""
        transcript_path = session_dir / "transcript.jsonl"
        if not transcript_path.exists():
            return []

        messages = []
        try:
            with open(transcript_path, "r") as f:
                for line in f:
                    if line.strip():
                        messages.append(json.loads(line))
        except Exception as e:
            print(f"Error parsing transcript {transcript_path}: {e}")

        return messages

    def detect_delegation_pattern(self, messages: List[Dict]) -> Dict[str, Any]:
        """Detect agent delegation patterns."""
        agents_used = []
        delegation_count = 0

        for msg in messages:
            content = msg.get("content", "")

            # Look for agent delegation in user messages
            if msg.get("role") == "user" and isinstance(content, str):
                if "use " in content.lower() and "agent" in content.lower():
                    delegation_count += 1
                    # Extract agent name
                    match = re.search(r"use\s+(\S+)", content, re.IGNORECASE)
                    if match:
                        agents_used.append(match.group(1))

            # Look for tool calls to agents
            if msg.get("role") == "assistant":
                tool_calls = msg.get("tool_calls", [])
                if tool_calls:
                    for call in tool_calls:
                        tool_name = call.get("tool", "")
                        if "agent" in tool_name or "delegate" in tool_name:
                            delegation_count += 1

        return {
            "delegation_count": delegation_count,
            "agents_used": list(set(agents_used)),
            "has_delegation": delegation_count > 0,
        }

    def detect_iteration_pattern(self, messages: List[Dict]) -> Dict[str, Any]:
        """Detect iterative refinement patterns."""
        iterations = 0
        refinement_keywords = [
            "refine",
            "improve",
            "fix",
            "update",
            "revise",
            "modify",
            "adjust",
            "correct",
        ]

        for msg in messages:
            if msg.get("role") == "user":
                content = str(msg.get("content", "")).lower()
                if any(keyword in content for keyword in refinement_keywords):
                    iterations += 1

        return {"iteration_count": iterations, "is_iterative": iterations >= 2}

    def detect_exploration_pattern(self, messages: List[Dict]) -> Dict[str, Any]:
        """Detect exploratory investigation patterns."""
        exploration_tools = ["read_file", "glob", "grep", "bash", "web_search"]
        tool_usage = Counter()
        parallel_searches = 0

        for msg in messages:
            if msg.get("role") == "assistant":
                tool_calls = msg.get("tool_calls", [])
                if len(tool_calls) > 1:
                    parallel_searches += 1

                for call in tool_calls:
                    tool = call.get("tool", "")
                    if tool in exploration_tools:
                        tool_usage[tool] += 1

        total_exploration = sum(tool_usage.values())

        return {
            "exploration_tool_count": total_exploration,
            "parallel_searches": parallel_searches,
            "is_exploratory": total_exploration >= 5 or parallel_searches >= 2,
            "tools_used": dict(tool_usage),
        }

    def detect_implementation_pattern(self, messages: List[Dict]) -> Dict[str, Any]:
        """Detect direct implementation patterns."""
        write_operations = 0
        edit_operations = 0

        for msg in messages:
            if msg.get("role") == "assistant":
                tool_calls = msg.get("tool_calls", [])
                for call in tool_calls:
                    tool = call.get("tool", "")
                    if tool == "write_file":
                        write_operations += 1
                    elif tool == "edit_file":
                        edit_operations += 1

        total_ops = write_operations + edit_operations

        return {
            "write_operations": write_operations,
            "edit_operations": edit_operations,
            "total_file_ops": total_ops,
            "is_implementation": total_ops >= 3,
        }

    def detect_error_recovery(self, messages: List[Dict]) -> Dict[str, Any]:
        """Detect error recovery approaches."""
        errors = 0
        recovery_attempts = 0

        for i, msg in enumerate(messages):
            if msg.get("role") == "tool":
                content = str(msg.get("content", ""))
                if "error" in content.lower() or "failed" in content.lower():
                    errors += 1
                    # Check if next assistant message attempts recovery
                    if (
                        i + 1 < len(messages)
                        and messages[i + 1].get("role") == "assistant"
                    ):
                        recovery_attempts += 1

        return {
            "errors_encountered": errors,
            "recovery_attempts": recovery_attempts,
            "has_error_recovery": errors > 0 and recovery_attempts > 0,
            "recovery_rate": recovery_attempts / errors if errors > 0 else 0,
        }

    def detect_planning_vs_execution(self, messages: List[Dict]) -> Dict[str, Any]:
        """Detect planning vs execution balance."""
        planning_messages = 0
        execution_messages = 0

        for msg in messages:
            if msg.get("role") == "assistant":
                content = msg.get("content", [])
                if isinstance(content, list):
                    for item in content:
                        if item.get("type") == "thinking":
                            planning_messages += 1
                        elif item.get("type") == "tool_call":
                            execution_messages += 1

        total = planning_messages + execution_messages
        planning_ratio = planning_messages / total if total > 0 else 0

        return {
            "planning_messages": planning_messages,
            "execution_messages": execution_messages,
            "planning_ratio": planning_ratio,
            "approach": "planning-heavy"
            if planning_ratio > 0.6
            else "execution-heavy"
            if planning_ratio < 0.3
            else "balanced",
        }

    def detect_validation_pattern(self, messages: List[Dict]) -> Dict[str, Any]:
        """Detect validation approaches."""
        test_runs = 0
        checks = 0
        reviews = 0

        for msg in messages:
            if msg.get("role") == "assistant":
                tool_calls = msg.get("tool_calls", [])
                for call in tool_calls:
                    tool = call.get("tool", "")
                    args = call.get("arguments", {})

                    if "test" in str(args).lower() or "test" in tool.lower():
                        test_runs += 1
                    if tool == "python_check":
                        checks += 1
                    if "review" in str(args).lower() or "review" in tool.lower():
                        reviews += 1

        total_validation = test_runs + checks + reviews

        return {
            "test_runs": test_runs,
            "code_checks": checks,
            "reviews": reviews,
            "total_validation": total_validation,
            "has_validation": total_validation > 0,
        }

    def calculate_session_duration(self, messages: List[Dict]) -> float:
        """Calculate session duration in minutes."""
        if len(messages) < 2:
            return 0

        try:
            first_ts = messages[0].get("timestamp", "")
            last_ts = messages[-1].get("timestamp", "")

            if first_ts and last_ts:
                first_time = datetime.fromisoformat(first_ts.replace("+00:00", ""))
                last_time = datetime.fromisoformat(last_ts.replace("+00:00", ""))
                duration = (last_time - first_time).total_seconds() / 60
                return round(duration, 2)
        except Exception:
            pass

        return 0

    def categorize_approach(self, patterns: Dict[str, Any]) -> List[str]:
        """Categorize the primary problem-solving approach(es)."""
        approaches = []

        if patterns["iteration"]["is_iterative"]:
            approaches.append("Iterative Refinement")

        if patterns["exploration"]["is_exploratory"]:
            approaches.append("Exploratory Investigation")

        if (
            patterns["implementation"]["is_implementation"]
            and not patterns["iteration"]["is_iterative"]
        ):
            approaches.append("Direct Implementation")

        if patterns["delegation"]["has_delegation"]:
            approaches.append("Multi-Agent Orchestration")

        if patterns["error_recovery"]["has_error_recovery"]:
            approaches.append("Error Recovery & Resilience")

        if patterns["validation"]["has_validation"]:
            approaches.append("Validation-Driven")

        if not approaches:
            approaches.append("Simple/Conversational")

        return approaches

    def analyze_session(self, metadata_path: Path) -> Dict[str, Any] | None:
        """Analyze a single session."""
        metadata = self.parse_metadata(metadata_path)
        session_dir = metadata_path.parent
        messages = self.parse_transcript(session_dir)

        if not metadata or not messages:
            return None

        # Detect patterns
        patterns = {
            "delegation": self.detect_delegation_pattern(messages),
            "iteration": self.detect_iteration_pattern(messages),
            "exploration": self.detect_exploration_pattern(messages),
            "implementation": self.detect_implementation_pattern(messages),
            "error_recovery": self.detect_error_recovery(messages),
            "planning_execution": self.detect_planning_vs_execution(messages),
            "validation": self.detect_validation_pattern(messages),
        }

        duration = self.calculate_session_duration(messages)
        approaches = self.categorize_approach(patterns)

        # Determine success indicators
        success_indicators = []
        if patterns["implementation"]["total_file_ops"] > 0:
            success_indicators.append("Files Modified")
        if patterns["error_recovery"]["recovery_rate"] > 0.5:
            success_indicators.append("Good Error Recovery")
        if patterns["validation"]["has_validation"]:
            success_indicators.append("Validated")
        if metadata.get("turn_count", 0) > 5:
            success_indicators.append("Substantial Work")

        return {
            "session_id": metadata.get("session_id", ""),
            "parent_session_id": session_dir.name.split("-")[0]
            if "-" in session_dir.name
            else "",
            "created": metadata.get("created", ""),
            "name": metadata.get("name", "Untitled"),
            "description": metadata.get("description", "")[:200],
            "bundle": metadata.get("bundle", ""),
            "model": metadata.get("model", ""),
            "turn_count": metadata.get("turn_count", 0),
            "message_count": len(messages),
            "duration_minutes": duration,
            "approaches": approaches,
            "primary_approach": approaches[0] if approaches else "Unknown",
            "patterns": patterns,
            "success_indicators": success_indicators,
            "project": str(metadata_path)
            .split("/projects/")[-1]
            .split("/sessions/")[0],
        }

    def analyze_all_sessions(self) -> List[Dict[str, Any]]:
        """Analyze all sessions."""
        metadata_files = self.find_all_sessions()
        print(f"Found {len(metadata_files)} sessions to analyze...")

        results = []
        for i, metadata_path in enumerate(metadata_files):
            if i % 10 == 0:
                print(f"Progress: {i}/{len(metadata_files)}")

            result = self.analyze_session(metadata_path)
            if result:
                results.append(result)

        return results

    def generate_summary_statistics(self, sessions: List[Dict]) -> Dict[str, Any]:
        """Generate summary statistics."""
        approach_counts = Counter()
        for session in sessions:
            for approach in session["approaches"]:
                approach_counts[approach] += 1

        # Calculate averages
        avg_turns = (
            sum(s["turn_count"] for s in sessions) / len(sessions) if sessions else 0
        )
        avg_duration = (
            sum(s["duration_minutes"] for s in sessions) / len(sessions)
            if sessions
            else 0
        )

        # Pattern frequencies
        pattern_stats = {
            "iterative_sessions": sum(
                1 for s in sessions if s["patterns"]["iteration"]["is_iterative"]
            ),
            "exploratory_sessions": sum(
                1 for s in sessions if s["patterns"]["exploration"]["is_exploratory"]
            ),
            "implementation_sessions": sum(
                1
                for s in sessions
                if s["patterns"]["implementation"]["is_implementation"]
            ),
            "delegated_sessions": sum(
                1 for s in sessions if s["patterns"]["delegation"]["has_delegation"]
            ),
            "validated_sessions": sum(
                1 for s in sessions if s["patterns"]["validation"]["has_validation"]
            ),
            "error_recovery_sessions": sum(
                1
                for s in sessions
                if s["patterns"]["error_recovery"]["has_error_recovery"]
            ),
        }

        # Time trends
        sessions_by_date = defaultdict(list)
        for session in sessions:
            date = session["created"][:10] if session["created"] else "unknown"
            sessions_by_date[date].append(session)

        return {
            "total_sessions": len(sessions),
            "approach_frequencies": dict(approach_counts),
            "average_turns": round(avg_turns, 2),
            "average_duration_minutes": round(avg_duration, 2),
            "pattern_statistics": pattern_stats,
            "sessions_by_date": {
                date: len(sess) for date, sess in sorted(sessions_by_date.items())
            },
        }

    def export_to_json(self, sessions: List[Dict], summary: Dict, output_path: str):
        """Export results to JSON."""
        output = {
            "generated_at": datetime.now().isoformat(),
            "summary_statistics": summary,
            "sessions": sessions,
        }

        with open(output_path, "w") as f:
            json.dump(output, f, indent=2)

        print(f"\n✅ Exported to {output_path}")

    def export_to_csv(self, sessions: List[Dict], output_path: str):
        """Export sessions to CSV for Excel."""
        import csv

        with open(output_path, "w", newline="") as f:
            writer = csv.writer(f)

            # Header
            writer.writerow(
                [
                    "Session ID",
                    "Parent Session",
                    "Created",
                    "Name",
                    "Project",
                    "Bundle",
                    "Model",
                    "Turn Count",
                    "Message Count",
                    "Duration (min)",
                    "Primary Approach",
                    "All Approaches",
                    "Is Iterative",
                    "Iteration Count",
                    "Is Exploratory",
                    "Exploration Count",
                    "Has Delegation",
                    "Delegation Count",
                    "File Operations",
                    "Errors",
                    "Recovery Rate",
                    "Validation Count",
                    "Planning Ratio",
                    "Success Indicators",
                ]
            )

            # Data rows
            for s in sessions:
                writer.writerow(
                    [
                        s["session_id"],
                        s["parent_session_id"],
                        s["created"],
                        s["name"],
                        s["project"],
                        s["bundle"],
                        s["model"],
                        s["turn_count"],
                        s["message_count"],
                        s["duration_minutes"],
                        s["primary_approach"],
                        ", ".join(s["approaches"]),
                        s["patterns"]["iteration"]["is_iterative"],
                        s["patterns"]["iteration"]["iteration_count"],
                        s["patterns"]["exploration"]["is_exploratory"],
                        s["patterns"]["exploration"]["exploration_tool_count"],
                        s["patterns"]["delegation"]["has_delegation"],
                        s["patterns"]["delegation"]["delegation_count"],
                        s["patterns"]["implementation"]["total_file_ops"],
                        s["patterns"]["error_recovery"]["errors_encountered"],
                        s["patterns"]["error_recovery"]["recovery_rate"],
                        s["patterns"]["validation"]["total_validation"],
                        round(s["patterns"]["planning_execution"]["planning_ratio"], 2),
                        ", ".join(s["success_indicators"]),
                    ]
                )

        print(f"✅ Exported to {output_path}")


def main():
    projects_dir = os.path.expanduser("~/.amplifier/projects")

    analyzer = SessionAnalyzer(projects_dir)

    print("🔍 Analyzing Amplifier sessions...")
    sessions = analyzer.analyze_all_sessions()

    print("\n📊 Generating summary statistics...")
    summary = analyzer.generate_summary_statistics(sessions)

    # Export results
    output_dir = Path.cwd()
    analyzer.export_to_json(
        sessions, summary, str(output_dir / "session_analysis.json")
    )
    analyzer.export_to_csv(sessions, str(output_dir / "session_analysis.csv"))

    # Print summary
    print("\n" + "=" * 60)
    print("SUMMARY STATISTICS")
    print("=" * 60)
    print(f"Total Sessions Analyzed: {summary['total_sessions']}")
    print(f"Average Turns per Session: {summary['average_turns']}")
    print(f"Average Duration: {summary['average_duration_minutes']:.1f} minutes")
    print("\nApproach Frequencies:")
    for approach, count in sorted(
        summary["approach_frequencies"].items(), key=lambda x: x[1], reverse=True
    ):
        pct = (count / summary["total_sessions"]) * 100
        print(f"  {approach}: {count} ({pct:.1f}%)")

    print("\nPattern Statistics:")
    for pattern, count in summary["pattern_statistics"].items():
        pct = (count / summary["total_sessions"]) * 100
        print(f"  {pattern}: {count} ({pct:.1f}%)")

    print("\n" + "=" * 60)
    print("✨ Analysis complete!")


if __name__ == "__main__":
    main()
