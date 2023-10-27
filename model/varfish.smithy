$version: "2.0"

namespace com.github.bihealth.varfish

use aws.protocols#restJson1

/// Provides access to the VarFish API.
@restJson1
@httpApiKeyAuth(scheme: "Token", name: "Authorization", in: "header")
service VarFishService {
    version: "2023-10-27"
    operations: [
        CaseImportList
    ]
}

/// Input type for `CaseImportList`.
@input
structure CaseImportListInput {
    // Sent in the URI label named "projectUuid".
    @required
    @httpLabel
    projectUuid: String,

    @httpQuery("page")
    page: Integer,

    @httpQuery("page_size")
    pageSize: Integer,
}

/// Output type for `CaseImportList`.
@output
structure CaseImportListOutput {}

/// Returns case import actions for the given project using pagination.
@readonly
@http(uri: "/cases-import/api/case-import-action/list-create/{projectUuid}/", method: "GET", code: 200)
operation CaseImportList {
    input: CaseImportListInput
    output: CaseImportListOutput
}
