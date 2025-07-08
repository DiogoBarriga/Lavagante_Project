# Megalithic Yard System - API Reference

## 🗿 Complete API Documentation

Comprehensive API reference for all Megalithic Yard Integration System components.

---

## 📋 Table of Contents

1. [Core Components](#core-components)
2. [Analysis Engine](#analysis-engine)
3. [Visualization Engine](#visualization-engine)
4. [Reporting Engine](#reporting-engine)
5. [System Integrator](#system-integrator)
6. [Configuration Classes](#configuration-classes)
7. [Data Structures](#data-structures)
8. [Utility Functions](#utility-functions)
9. [Error Classes](#error-classes)

---

## 🏗️ Core Components

### MegalithicYardCore

The fundamental MY calculations and mathematical operations.

```python
class MegalithicYardCore:
    """Core Megalithic Yard calculations and constants."""
    
    # Constants
    MY_METER = 2.72                    # Standard MY in feet
    MY_METER_METERS = 0.8297          # MY in meters
    MY_METER_INCHES = 32.64           # MY in inches
    MY_METER_CM = 82.97               # MY in centimeters
    
    def __init__(self):
        """Initialize the MY core calculation engine."""
    
    def convert_my_to_units(self, my_value: float, unit: str = 'feet') -> float:
        """
        Convert MY value to specified units.
        
        Args:
            my_value (float): Value in MY units
            unit (str): Target unit ('feet', 'meters', 'inches', 'cm')
            
        Returns:
            float: Converted value in specified units
            
        Raises:
            ValueError: If unit is not supported
        """
    
    def convert_units_to_my(self, value: float, unit: str = 'feet') -> float:
        """
        Convert value from specified units to MY.
        
        Args:
            value (float): Value in specified units
            unit (str): Source unit ('feet', 'meters', 'inches', 'cm')
            
        Returns:
            float: Value in MY units
        """
    
    def calculate_my_harmonics(self, base_value: float, num_harmonics: int = 10) -> List[float]:
        """
        Calculate MY harmonic series for a base value.
        
        Args:
            base_value (float): Base value for harmonic calculation
            num_harmonics (int): Number of harmonics to calculate
            
        Returns:
            List[float]: List of harmonic values
        """
    
    def calculate_my_ratios(self, price_range: Tuple[float, float]) -> Dict[str, float]:
        """
        Calculate key MY ratios for a price range.
        
        Args:
            price_range (Tuple[float, float]): (min_price, max_price)
            
        Returns:
            Dict[str, float]: Dictionary of ratio levels
        """
    
    def get_my_cycles(self, timeframe: str = '1H') -> Dict[str, int]:
        """
        Get MY cycle periods for a timeframe.
        
        Args:
            timeframe (str): Market timeframe ('1M', '5M', '15M', '1H', '4H', '1D')
            
        Returns:
            Dict[str, int]: Cycle periods by type
        """
```

### MegalithicYardAnalyzer

Main analysis engine for MY calculations.

```python
class MegalithicYardAnalyzer:
    """Primary analysis engine for Megalithic Yard calculations."""
    
    def __init__(self, config: Optional[Dict] = None):
        """
        Initialize the MY analyzer.
        
        Args:
            config (Optional[Dict]): Configuration parameters
        """
    
    async def analyze_price_levels(self, data: pd.DataFrame, **kwargs) -> Dict[str, Any]:
        """
        Analyze price levels using MY calculations.
        
        Args:
            data (pd.DataFrame): Market data with OHLCV columns
            **kwargs: Additional analysis parameters
            
        Returns:
            Dict[str, Any]: Price level analysis results
        """
    
    async def detect_cycles(self, data: pd.DataFrame, cycle_types: List[str] = None) -> Dict[str, Any]:
        """
        Detect MY cycles in market data.
        
        Args:
            data (pd.DataFrame): Market data
            cycle_types (List[str]): Types of cycles to detect
            
        Returns:
            Dict[str, Any]: Cycle detection results
        """
    
    async def analyze_patterns(self, data: pd.DataFrame, min_confidence: float = 0.6) -> Dict[str, Any]:
        """
        Analyze geometric patterns using MY principles.
        
        Args:
            data (pd.DataFrame): Market data
            min_confidence (float): Minimum confidence threshold
            
        Returns:
            Dict[str, Any]: Pattern analysis results
        """
    
    async def calculate_confluence(self, data: pd.DataFrame, **kwargs) -> Dict[str, Any]:
        """
        Calculate MY confluence zones.
        
        Args:
            data (pd.DataFrame): Market data
            **kwargs: Confluence calculation parameters
            
        Returns:
            Dict[str, Any]: Confluence analysis results
        """
```

---

## 🔍 Analysis Engine

### EnhancedMYAnalyticsEngine

Advanced analytics engine with comprehensive MY analysis capabilities.

```python
class EnhancedMYAnalyticsEngine:
    """Enhanced MY analytics engine with advanced capabilities."""
    
    def __init__(self, config: Optional[MYAnalyticsConfig] = None):
        """
        Initialize the enhanced analytics engine.
        
        Args:
            config (Optional[MYAnalyticsConfig]): Engine configuration
        """
    
    async def comprehensive_analysis(
        self,
        data: pd.DataFrame,
        symbol: str,
        timeframe: str = '1H',
        **kwargs
    ) -> MYAnalysisResult:
        """
        Perform comprehensive MY analysis.
        
        Args:
            data (pd.DataFrame): Market data
            symbol (str): Trading symbol
            timeframe (str): Data timeframe
            **kwargs: Additional analysis parameters
            
        Returns:
            MYAnalysisResult: Complete analysis results
        """
    
    async def quick_analysis(
        self,
        data: pd.DataFrame,
        symbol: str,
        focus: str = 'confluence'
    ) -> MYQuickResult:
        """
        Perform quick MY analysis focused on specific aspect.
        
        Args:
            data (pd.DataFrame): Market data
            symbol (str): Trading symbol
            focus (str): Analysis focus ('confluence', 'cycles', 'patterns')
            
        Returns:
            MYQuickResult: Quick analysis results
        """
    
    async def backtest_analysis(
        self,
        data: pd.DataFrame,
        strategy_config: Dict[str, Any],
        **kwargs
    ) -> MYBacktestResult:
        """
        Perform backtesting using MY analytics.
        
        Args:
            data (pd.DataFrame): Historical market data
            strategy_config (Dict[str, Any]): Strategy configuration
            **kwargs: Backtesting parameters
            
        Returns:
            MYBacktestResult: Backtest results
        """
    
    def validate_data(self, data: pd.DataFrame) -> MYDataValidation:
        """
        Validate market data for MY analysis.
        
        Args:
            data (pd.DataFrame): Market data to validate
            
        Returns:
            MYDataValidation: Validation results
        """
    
    def get_supported_timeframes(self) -> List[str]:
        """
        Get list of supported timeframes.
        
        Returns:
            List[str]: Supported timeframes
        """
```

### MYAnalysisResult

Primary result structure for MY analysis.

```python
@dataclass
class MYAnalysisResult:
    """Complete MY analysis result structure."""
    
    # Basic Information
    symbol: str
    timeframe: str
    analysis_timestamp: datetime
    data_range: Tuple[datetime, datetime]
    
    # MY Calculations
    my_levels: Dict[str, Any]           # Price levels based on MY ratios
    my_harmonics: List[float]           # Harmonic series
    my_cycles: Dict[str, Any]           # Detected cycles
    my_ratios: Dict[str, float]         # Key ratios
    
    # Analysis Results
    patterns: List[Dict[str, Any]]      # Geometric patterns
    signals: List[Dict[str, Any]]       # Trading signals
    confluence_zones: List[Dict[str, Any]]  # High-probability zones
    
    # Performance Metrics
    accuracy_score: float               # Historical accuracy
    confidence_level: float             # Analysis confidence
    reliability_score: float            # Result reliability
    
    # Risk Assessment
    risk_assessment: Dict[str, Any]     # Risk metrics
    volatility_analysis: Dict[str, Any] # Volatility assessment
    
    # Integration Data
    quantum_integration: Optional[Dict] # Quantum analysis integration
    fibonacci_integration: Optional[Dict] # Fibonacci integration
    phi_enhancement: Optional[Dict]     # φ enhancement data
    
    # Metadata
    processing_time: float              # Analysis duration
    cache_used: bool                   # Whether cache was used
    warnings: List[str]                # Analysis warnings
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert result to dictionary format."""
    
    def to_json(self) -> str:
        """Convert result to JSON string."""
    
    def get_summary(self) -> str:
        """Get text summary of analysis."""
    
    def get_key_levels(self, count: int = 5) -> List[Dict[str, Any]]:
        """Get top key levels by importance."""
    
    def get_active_patterns(self) -> List[Dict[str, Any]]:
        """Get currently active patterns."""
    
    def get_confluence_score(self) -> float:
        """Get overall confluence score."""
```

---

## 📊 Visualization Engine

### MYVisualizationEngine

Advanced visualization system for MY analytics.

```python
class MYVisualizationEngine:
    """Advanced visualization engine for MY analytics."""
    
    def __init__(self, config: Optional[MYVisualizationConfig] = None):
        """
        Initialize visualization engine.
        
        Args:
            config (Optional[MYVisualizationConfig]): Visualization configuration
        """
    
    async def create_price_chart(
        self,
        data: pd.DataFrame,
        results: MYAnalysisResult,
        config: Optional[Dict] = None
    ) -> MYVisualizationResult:
        """
        Create price action chart with MY overlays.
        
        Args:
            data (pd.DataFrame): Market data
            results (MYAnalysisResult): Analysis results
            config (Optional[Dict]): Chart configuration
            
        Returns:
            MYVisualizationResult: Chart creation results
        """
    
    async def create_harmonic_3d(
        self,
        results: MYAnalysisResult,
        config: Optional[Dict] = None
    ) -> MYVisualizationResult:
        """
        Create 3D harmonic visualization.
        
        Args:
            results (MYAnalysisResult): Analysis results
            config (Optional[Dict]): 3D visualization configuration
            
        Returns:
            MYVisualizationResult: 3D chart results
        """
    
    async def create_confluence_heatmap(
        self,
        results: MYAnalysisResult,
        resolution: str = 'medium'
    ) -> MYVisualizationResult:
        """
        Create confluence zone heatmap.
        
        Args:
            results (MYAnalysisResult): Analysis results
            resolution (str): Heatmap resolution ('low', 'medium', 'high')
            
        Returns:
            MYVisualizationResult: Heatmap results
        """
    
    async def create_cycle_visualization(
        self,
        results: MYAnalysisResult,
        cycle_types: List[str] = None
    ) -> MYVisualizationResult:
        """
        Create cycle analysis visualization.
        
        Args:
            results (MYAnalysisResult): Analysis results
            cycle_types (List[str]): Cycle types to visualize
            
        Returns:
            MYVisualizationResult: Cycle chart results
        """
    
    async def create_pattern_overlay(
        self,
        data: pd.DataFrame,
        results: MYAnalysisResult,
        pattern_types: List[str] = None
    ) -> MYVisualizationResult:
        """
        Create pattern overlay visualization.
        
        Args:
            data (pd.DataFrame): Market data
            results (MYAnalysisResult): Analysis results
            pattern_types (List[str]): Pattern types to overlay
            
        Returns:
            MYVisualizationResult: Pattern overlay results
        """
    
    def get_available_themes(self) -> List[str]:
        """Get list of available visualization themes."""
    
    def get_export_formats(self) -> List[str]:
        """Get list of supported export formats."""
```

### MYVisualizationConfig

Configuration class for visualization settings.

```python
@dataclass
class MYVisualizationConfig:
    """Configuration for MY visualization engine."""
    
    # Chart Settings
    theme: str = 'professional'          # Chart theme
    color_scheme: str = 'default'        # Color scheme
    resolution: str = 'high'             # Chart resolution
    interactive: bool = True             # Interactive charts
    
    # Layout Settings
    chart_width: int = 1200             # Chart width in pixels
    chart_height: int = 800             # Chart height in pixels
    margin_top: int = 50                # Top margin
    margin_bottom: int = 100            # Bottom margin
    margin_left: int = 80               # Left margin
    margin_right: int = 80              # Right margin
    
    # MY Specific Settings
    show_my_levels: bool = True         # Show MY price levels
    show_harmonics: bool = True         # Show harmonic series
    show_cycles: bool = True            # Show cycle analysis
    show_patterns: bool = True          # Show pattern recognition
    show_confluence: bool = True        # Show confluence zones
    
    # Export Settings
    export_formats: List[str] = None    # Export formats
    export_directory: str = './charts'  # Export directory
    filename_template: str = '{symbol}_{timeframe}_{type}_{timestamp}'
    
    # Performance Settings
    max_data_points: int = 10000        # Maximum data points to plot
    use_sampling: bool = True           # Use data sampling for large datasets
    cache_charts: bool = True           # Cache generated charts
```

---

## 📑 Reporting Engine

### MYReportingEngine

Professional reporting system for MY analytics.

```python
class MYReportingEngine:
    """Professional reporting engine for MY analytics."""
    
    def __init__(self, config: Optional[MYReportConfig] = None):
        """
        Initialize reporting engine.
        
        Args:
            config (Optional[MYReportConfig]): Report configuration
        """
    
    async def generate_report(
        self,
        results: Union[MYAnalysisResult, List[MYAnalysisResult]],
        template: str = 'executive',
        format: str = 'pdf',
        **kwargs
    ) -> MYReportResult:
        """
        Generate professional MY analysis report.
        
        Args:
            results: Analysis results (single or multiple)
            template (str): Report template type
            format (str): Output format ('pdf', 'html', 'excel', 'json')
            **kwargs: Additional report parameters
            
        Returns:
            MYReportResult: Report generation results
        """
    
    async def generate_executive_summary(
        self,
        results: MYAnalysisResult,
        **kwargs
    ) -> MYReportResult:
        """
        Generate executive summary report.
        
        Args:
            results (MYAnalysisResult): Analysis results
            **kwargs: Summary parameters
            
        Returns:
            MYReportResult: Executive summary results
        """
    
    async def generate_technical_report(
        self,
        results: MYAnalysisResult,
        detailed: bool = True
    ) -> MYReportResult:
        """
        Generate detailed technical analysis report.
        
        Args:
            results (MYAnalysisResult): Analysis results
            detailed (bool): Include detailed analysis
            
        Returns:
            MYReportResult: Technical report results
        """
    
    async def generate_multi_symbol_report(
        self,
        results: Dict[str, MYAnalysisResult],
        comparison: bool = True
    ) -> MYReportResult:
        """
        Generate multi-symbol comparison report.
        
        Args:
            results (Dict[str, MYAnalysisResult]): Results by symbol
            comparison (bool): Include comparison analysis
            
        Returns:
            MYReportResult: Multi-symbol report results
        """
    
    async def generate_backtest_report(
        self,
        backtest_results: MYBacktestResult,
        **kwargs
    ) -> MYReportResult:
        """
        Generate backtesting performance report.
        
        Args:
            backtest_results (MYBacktestResult): Backtest results
            **kwargs: Report parameters
            
        Returns:
            MYReportResult: Backtest report results
        """
    
    def get_available_templates(self) -> List[str]:
        """Get list of available report templates."""
    
    def get_supported_formats(self) -> List[str]:
        """Get list of supported export formats."""
```

---

## 🎛️ System Integrator

### MYSystemIntegrator

Central controller for the complete MY system.

```python
class MYSystemIntegrator:
    """Central controller for the complete MY system."""
    
    def __init__(self, config: Optional[MYSystemConfig] = None):
        """
        Initialize the MY system integrator.
        
        Args:
            config (Optional[MYSystemConfig]): System configuration
        """
    
    async def run_comprehensive_analysis(
        self,
        data: pd.DataFrame,
        symbol: str,
        timeframe: str = '1H',
        **kwargs
    ) -> MYAnalysisResult:
        """
        Run comprehensive MY analysis through the complete system.
        
        Args:
            data (pd.DataFrame): Market data
            symbol (str): Trading symbol
            timeframe (str): Data timeframe
            **kwargs: Analysis parameters
            
        Returns:
            MYAnalysisResult: Complete analysis results
        """
    
    async def create_visualization(
        self,
        results: MYAnalysisResult,
        chart_type: str = 'price_action',
        **kwargs
    ) -> MYVisualizationResult:
        """
        Create visualization through the visualization engine.
        
        Args:
            results (MYAnalysisResult): Analysis results
            chart_type (str): Type of chart to create
            **kwargs: Visualization parameters
            
        Returns:
            MYVisualizationResult: Visualization results
        """
    
    async def generate_report(
        self,
        results: MYAnalysisResult,
        template: str = 'executive',
        format: str = 'pdf',
        **kwargs
    ) -> MYReportResult:
        """
        Generate report through the reporting engine.
        
        Args:
            results (MYAnalysisResult): Analysis results
            template (str): Report template
            format (str): Output format
            **kwargs: Report parameters
            
        Returns:
            MYReportResult: Report generation results
        """
    
    async def analyze_symbol(
        self,
        symbol: str,
        timeframe: str = '1H',
        periods: int = 500,
        **kwargs
    ) -> MYAnalysisResult:
        """
        Analyze a trading symbol with automatic data retrieval.
        
        Args:
            symbol (str): Trading symbol
            timeframe (str): Data timeframe
            periods (int): Number of periods to analyze
            **kwargs: Analysis parameters
            
        Returns:
            MYAnalysisResult: Analysis results
        """
    
    def check_system_health(self) -> MYSystemHealth:
        """
        Check the health status of all system components.
        
        Returns:
            MYSystemHealth: System health status
        """
    
    def get_configuration(self) -> MYSystemConfig:
        """Get current system configuration."""
    
    def update_configuration(self, updates: Dict[str, Any]) -> None:
        """Update system configuration."""
    
    def save_configuration(self, filepath: str) -> None:
        """Save current configuration to file."""
    
    def load_configuration(self, filepath: str) -> None:
        """Load configuration from file."""
```

---

## ⚙️ Configuration Classes

### MYSystemConfig

Main system configuration class.

```python
@dataclass
class MYSystemConfig:
    """Configuration for the complete MY system."""
    
    # Component enablement
    analytics_enabled: bool = True
    visualization_enabled: bool = True
    reporting_enabled: bool = True
    performance_optimization_enabled: bool = True
    
    # System settings
    auto_startup: bool = True
    health_monitoring: bool = True
    error_recovery: bool = True
    debug_mode: bool = False
    
    # Performance settings
    max_concurrent_analyses: int = 3
    analysis_timeout_seconds: int = 30
    cache_enabled: bool = True
    async_processing: bool = True
    
    # Integration settings
    desktop_integration: bool = True
    standalone_mode: bool = False
    auto_save_results: bool = True
    export_formats: List[str] = None
    
    # Monitoring settings
    performance_tracking: bool = True
    error_logging: bool = True
    usage_analytics: bool = False
    
    def validate(self) -> List[str]:
        """Validate configuration and return any issues."""
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary."""
    
    def from_dict(self, config_dict: Dict[str, Any]) -> None:
        """Load configuration from dictionary."""
```

### MYAnalyticsConfig

Configuration for the analytics engine.

```python
@dataclass
class MYAnalyticsConfig:
    """Configuration for MY analytics engine."""
    
    # Analysis settings
    default_timeframe: str = '1H'
    max_lookback_periods: int = 1000
    min_confidence_threshold: float = 0.6
    
    # Integration settings
    enable_quantum_integration: bool = True
    enable_fibonacci_integration: bool = True
    enable_phi_enhancement: bool = True
    
    # Cycle analysis
    cycle_types: List[str] = None
    cycle_depth: int = 5
    cycle_confidence_threshold: float = 0.7
    
    # Pattern recognition
    pattern_types: List[str] = None
    pattern_confidence_threshold: float = 0.65
    geometric_tolerance: float = 0.05
    
    # Confluence analysis
    confluence_window: int = 10
    confluence_threshold: float = 0.75
    max_confluence_levels: int = 20
    
    # Performance
    cache_analysis_results: bool = True
    parallel_processing: bool = True
    max_processing_threads: int = 4
```

---

## 📊 Data Structures

### Core Data Classes

```python
@dataclass
class MYLevel:
    """Megalithic Yard price level."""
    price: float
    type: str                    # 'support', 'resistance', 'harmonic'
    strength: float             # 0.0 to 1.0
    confidence: float           # 0.0 to 1.0
    my_ratio: float            # MY ratio used for calculation
    timestamp: datetime        # When level was calculated
    
@dataclass
class MYCycle:
    """Megalithic Yard cycle information."""
    type: str                  # 'micro', 'short', 'medium', 'macro'
    period: int               # Cycle period in bars
    phase: float              # Current phase (0.0 to 1.0)
    strength: float           # Cycle strength (0.0 to 1.0)
    next_turn: datetime       # Predicted next cycle turn
    confidence: float         # Cycle confidence (0.0 to 1.0)
    
@dataclass
class MYPattern:
    """Megalithic Yard pattern information."""
    name: str                 # Pattern name
    type: str                 # 'geometric', 'harmonic', 'confluence'
    confidence: float         # Pattern confidence (0.0 to 1.0)
    completion: float         # Pattern completion (0.0 to 1.0)
    target_price: Optional[float]  # Price target
    target_time: Optional[datetime]  # Time target
    points: List[Tuple[datetime, float]]  # Pattern points
    
@dataclass
class MYSignal:
    """Trading signal from MY analysis."""
    type: str                 # 'buy', 'sell', 'neutral'
    strength: float           # Signal strength (0.0 to 1.0)
    confidence: float         # Signal confidence (0.0 to 1.0)
    entry_price: float        # Suggested entry price
    stop_loss: Optional[float]  # Stop loss level
    take_profit: Optional[float]  # Take profit level
    timestamp: datetime       # Signal timestamp
    reason: str               # Signal reason/description
```

### Result Classes

```python
@dataclass
class MYVisualizationResult:
    """Result from visualization creation."""
    success: bool
    chart_type: str
    output_path: str
    format: str
    file_size: int
    generation_time: float
    interactive: bool
    errors: List[str]
    
@dataclass
class MYReportResult:
    """Result from report generation."""
    success: bool
    template: str
    format: str
    output_path: str
    file_size: int
    generation_time: float
    pages: int
    sections: List[str]
    errors: List[str]
    
@dataclass
class MYSystemHealth:
    """System health status."""
    overall_status: str        # 'healthy', 'warning', 'error'
    component_status: Dict[str, str]  # Status by component
    performance_metrics: Dict[str, float]
    errors: List[str]
    warnings: List[str]
    last_check: datetime
    uptime: timedelta
```

---

## 🛠️ Utility Functions

### Data Utilities

```python
def validate_market_data(data: pd.DataFrame) -> Tuple[bool, List[str]]:
    """
    Validate market data format and completeness.
    
    Args:
        data (pd.DataFrame): Market data to validate
        
    Returns:
        Tuple[bool, List[str]]: (is_valid, list_of_issues)
    """

def clean_market_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and prepare market data for MY analysis.
    
    Args:
        data (pd.DataFrame): Raw market data
        
    Returns:
        pd.DataFrame: Cleaned market data
    """

def resample_data(data: pd.DataFrame, target_timeframe: str) -> pd.DataFrame:
    """
    Resample market data to target timeframe.
    
    Args:
        data (pd.DataFrame): Source market data
        target_timeframe (str): Target timeframe
        
    Returns:
        pd.DataFrame: Resampled data
    """
```

### MY Calculation Utilities

```python
def calculate_my_distance(price1: float, price2: float) -> float:
    """Calculate distance between prices in MY units."""

def find_nearest_my_level(price: float, levels: List[float]) -> float:
    """Find the nearest MY level to a given price."""

def calculate_my_confluence(levels: List[MYLevel], window: int = 10) -> List[Dict]:
    """Calculate confluence zones from MY levels."""

def convert_timeframe_to_my_cycles(timeframe: str) -> Dict[str, int]:
    """Convert timeframe to appropriate MY cycle periods."""
```

### Performance Utilities

```python
async def measure_execution_time(func: Callable, *args, **kwargs) -> Tuple[Any, float]:
    """Measure execution time of an async function."""

def optimize_data_for_analysis(data: pd.DataFrame, max_points: int = 5000) -> pd.DataFrame:
    """Optimize data size for analysis performance."""

def cache_analysis_result(key: str, result: MYAnalysisResult, ttl: int = 3600) -> None:
    """Cache analysis result with TTL."""

def get_cached_analysis_result(key: str) -> Optional[MYAnalysisResult]:
    """Retrieve cached analysis result."""
```

---

## ❌ Error Classes

### Custom Exception Classes

```python
class MYError(Exception):
    """Base exception for MY system errors."""
    pass

class MYAnalysisError(MYError):
    """Exception raised during MY analysis."""
    def __init__(self, message: str, analysis_type: str = None, symbol: str = None):
        self.analysis_type = analysis_type
        self.symbol = symbol
        super().__init__(message)

class MYDataError(MYError):
    """Exception raised for data-related issues."""
    def __init__(self, message: str, data_issue: str = None):
        self.data_issue = data_issue
        super().__init__(message)

class MYVisualizationError(MYError):
    """Exception raised during visualization creation."""
    def __init__(self, message: str, chart_type: str = None):
        self.chart_type = chart_type
        super().__init__(message)

class MYReportError(MYError):
    """Exception raised during report generation."""
    def __init__(self, message: str, report_format: str = None):
        self.report_format = report_format
        super().__init__(message)

class MYConfigurationError(MYError):
    """Exception raised for configuration issues."""
    def __init__(self, message: str, config_key: str = None):
        self.config_key = config_key
        super().__init__(message)

class MYSystemError(MYError):
    """Exception raised for system-level issues."""
    def __init__(self, message: str, component: str = None):
        self.component = component
        super().__init__(message)
```

---

## 📖 Usage Examples

### Basic API Usage

```python
# Initialize system
from my_system_integrator import MYSystemIntegrator
import pandas as pd

# Create system instance
my_system = MYSystemIntegrator()

# Load data
df = pd.read_csv('market_data.csv')

# Run analysis
results = await my_system.run_comprehensive_analysis(
    data=df,
    symbol='EURUSD',
    timeframe='1H'
)

# Create visualization
chart = await my_system.create_visualization(
    results=results,
    chart_type='price_action'
)

# Generate report
report = await my_system.generate_report(
    results=results,
    template='executive',
    format='pdf'
)
```

### Advanced Configuration

```python
# Custom configuration
config = MYSystemConfig(
    analytics_enabled=True,
    visualization_enabled=True,
    performance_optimization_enabled=True,
    max_concurrent_analyses=5,
    cache_enabled=True
)

# Initialize with custom config
my_system = MYSystemIntegrator(config=config)

# Custom analysis configuration
analysis_config = MYAnalyticsConfig(
    min_confidence_threshold=0.8,
    enable_quantum_integration=True,
    cycle_types=['micro', 'short', 'medium'],
    pattern_confidence_threshold=0.75
)

# Run analysis with custom config
results = await my_system.run_comprehensive_analysis(
    data=df,
    symbol='EURUSD',
    analysis_config=analysis_config
)
```

---

## 🔍 Method Reference Summary

### Quick Reference by Component

**MYSystemIntegrator**:
- `run_comprehensive_analysis()` - Full MY analysis
- `create_visualization()` - Chart generation
- `generate_report()` - Report creation
- `check_system_health()` - Health monitoring

**EnhancedMYAnalyticsEngine**:
- `comprehensive_analysis()` - Complete analysis
- `quick_analysis()` - Fast analysis
- `backtest_analysis()` - Strategy backtesting
- `validate_data()` - Data validation

**MYVisualizationEngine**:
- `create_price_chart()` - Price action charts
- `create_harmonic_3d()` - 3D visualizations
- `create_confluence_heatmap()` - Heatmaps
- `create_cycle_visualization()` - Cycle charts

**MYReportingEngine**:
- `generate_report()` - General reports
- `generate_executive_summary()` - Executive summaries
- `generate_technical_report()` - Technical reports
- `generate_backtest_report()` - Backtest reports

---

*🗿 Complete API Reference - Megalithic Yard Integration System*
