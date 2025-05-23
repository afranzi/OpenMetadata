#  Copyright 2025 Collate
#  Licensed under the Collate Community License, Version 1.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  https://github.com/open-metadata/OpenMetadata/blob/main/ingestion/LICENSE
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
"""
Superset utils module
"""

from typing import Optional

from metadata.generated.schema.entity.data.dashboardDataModel import DashboardDataModel


def get_dashboard_data_model_column_fqn(
    dashboard_data_model_entity: DashboardDataModel, column: str
) -> Optional[str]:
    """
    Get fqn of column if exist in dashboard data model entity.

    This is Superset implementation specific as table name is stored within displayName (table name contains
    numerical id), which is not consistent with implementations of dashboard data model columns of
    other dashboard sources.
    """
    if not dashboard_data_model_entity:
        return None
    for dashboard_data_model_column in dashboard_data_model_entity.columns:
        if column.lower() == dashboard_data_model_column.displayName.lower():
            return dashboard_data_model_column.fullyQualifiedName.root

    return None
