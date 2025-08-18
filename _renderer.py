"""
Custom quartodoc renderer to improve Returns section formatting.
"""

from quartodoc import MdRenderer
from plum import dispatch
from griffe import DocstringSectionReturns


class Renderer(MdRenderer):
    """Custom renderer with improved Returns section formatting."""
    style = "custom"
    
    @dispatch
    def render(self, el: DocstringSectionReturns):
        """Render Returns section with proper bullet list formatting."""
        # Get the default rendering first
        default_content = super().render(el)
        
        # Check if this is our EPBTTestResult returns section
        if "EPBTTestResult" in default_content:
            # Create a custom bullet list for the Returns section
            lines = [
                "| Name | Type | Description |",
                "|------|------|-------------|",
                "| | EPBTTestResult | Results object with the following attributes: |",
                "",
                "**Attributes:**",
                "",
                "- **n_rejected** (`int`): Number of hypotheses rejected at the specified alpha level",
                "- **pvalues** (`numpy.ndarray`): Empirical partially Bayes p-values for each test",  
                "- **adj_pvalues** (`numpy.ndarray`): Multiple testing corrected p-values (e.g., FDR-adjusted)",
                "- **reject** (`numpy.ndarray`): Boolean array indicating which hypotheses were rejected",
                "- **threshold** (`float`): P-value threshold used for rejection (largest rejected p-value)",
                "- **prior_fitted** (`object`): Fitted prior distribution object from Julia",
                ""
            ]
            return "\n".join(lines)
        
        # For other returns sections, use default rendering
        return default_content